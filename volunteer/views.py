from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404

# Create your views here.
from account.signals import task_evaluated
from core.models import Volunteer
from repository.models import Task, Project


def index_page(request):
    # todo(uda): view maybe?
    incompleted_project_tasks = Project.objects.filter(project_tasks__volunteer=get_volunteer(request),
                                                       project_tasks__is_negative=False,
                                                       project_tasks__is_neutral=False,
                                                       project_tasks__is_positive=False
                                                       )\
        .annotate(total=Coalesce(Count('project_tasks__volunteer'), 0))\
        .order_by('total')

    context = {'project_tasks': incompleted_project_tasks}
    return render(request, 'volunteer/index.html', context)


def play_page(request):
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
    volunteer = get_volunteer(request)
    task_count = Task.objects.filter(volunteer=volunteer, is_negative=False, is_neutral=False,
                                     is_positive=False).count()
    if task_count > 0:
        current_task = Task.objects.filter(volunteer=volunteer, is_negative=False, is_neutral=False, is_positive=False)[0]
    context = {'current_task': current_task, 'task_count': task_count}
    return render(request, 'volunteer/play.html', context)


def get_volunteer(request):
    return get_object_or_404(Volunteer, user=request.user)
