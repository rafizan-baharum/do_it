from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from account.models import Withdrawal
from account.signals import task_evaluated
from core.models import Doer
from doer.forms import WithdrawalModelForm
from repository.models import Task, Project


def index_page(request):
    # todo(uda): view maybe?

    incompleted_project_tasks = Project.objects.filter(project_tasks__doer=get_doer(request),
                                                       project_tasks__is_negative=False,
                                                       project_tasks__is_neutral=False,
                                                       project_tasks__is_positive=False
                                                       ) \
        .annotate(total=Coalesce(Count('project_tasks__doer'), 0)) \
        .order_by('total')
    recent_withdrawals = Withdrawal.objects.filter(doer=get_doer(request), status='APPROVED')[:5]

    doer = Doer.objects.filter(user_id=request.user.id).first()
    completed_task = Task.objects.filter(Q(doer_id=doer.user_id) &
                                         (Q(is_negative=True) |
                                          Q(is_positive=True) |
                                          Q(is_neutral=True))).count()

    collected_point_result = Task.objects.raw(
        f'select coalesce((count(t.id) * rp.task_point),0) as collected_point, t.id '
        'from repository_task t join repository_project rp on t.project_id = rp.id '
        'where t.doer_id = %s '
        'and (is_negative = 1 or is_positive= 1 or is_neutral=1) '
        'group by t.doer_id', [doer.user_id])

    collected_point = 0
    if len(collected_point_result) > 0:
        collected_point = collected_point_result[0].collected_point

    context = {
        'doer': doer,
        'completed_task': completed_task,
        'collected_point': collected_point,
        'earned': collected_point / 100,
        'recent_withdrawals': recent_withdrawals
    }

    # context = {
    #     'project_tasks': incompleted_project_tasks,
    #     'recent_withdrawals': recent_withdrawals,
    #     'current_user': request.user
    # }
    return render(request, 'doer/index.html', context)


def project_list_page(request):
    project_tasks = Project.objects.filter(project_tasks__doer=get_doer(request),
                                           project_tasks__is_negative=False,
                                           project_tasks__is_neutral=False,
                                           project_tasks__is_positive=False
                                           ) \
        .annotate(total=Coalesce(Count('project_tasks__doer'), 0)) \
        .order_by('total')
    context = {
        'project_tasks': project_tasks,
        'current_user': request.user
    }
    return render(request, 'doer/project_list.html', context)


def play_page(request, pk):
    current_task = None
    sentiment = request.POST.get('sentiment')
    task_id = request.POST.get('task_id')
    if sentiment:
        task = Task.objects.filter(pk=task_id).first()
        if sentiment == 'negative':
            Task.objects.filter(pk=task_id).update(is_negative=True)
            task_evaluated.send(sender=None, task=task)
        elif sentiment == 'neutral':
            Task.objects.filter(pk=task_id).update(is_neutral=True)
            task_evaluated.send(sender=None, task=task)
        elif sentiment == 'positive':
            Task.objects.filter(pk=task_id).update(is_positive=True)
            task_evaluated.send(sender=None, task=task)
        else:
            pass
    doer = get_doer(request)
    project = Project.objects.filter(pk=pk).first()
    task_count = Task.objects.filter(
        project=project,
        doer=doer,
        is_negative=False,
        is_neutral=False,
        is_positive=False).count()
    if task_count > 0:
        current_task = Task.objects.filter(
            project=project,
            doer=doer,
            is_negative=False,
            is_neutral=False,
            is_positive=False)[0]
    context = {
        'project': project,
        'current_task': current_task,
        'task_count': task_count,
        'current_user': request.user
    }
    return render(request, 'doer/play.html', context)


def withdrawal_list_page(request):
    withdrawals = Withdrawal.objects.filter(doer=get_doer(request)).order_by('-created_date')
    context = {
        'withdrawals': withdrawals,
    }
    return render(request, 'doer/withdrawal_list.html', context)


def withdrawal_create_page(request):
    form = WithdrawalModelForm(request.POST or None, initial={'amount': '10.00'})
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.doer = get_doer(request)
        obj.save()
        return redirect('doer:withdrawal_list')
    else:
        return render(request, 'doer/withdrawal_create.html', context)


def withdrawal_detail_page(request, pk):
    withdrawal = Withdrawal.objects.filter(pk=pk).first()
    context = {
        'withdrawal': withdrawal,
    }
    return render(request, 'doer/withdrawal_detail.html', context)


def get_doer(request):
    return get_object_or_404(Doer, user=request.user)
