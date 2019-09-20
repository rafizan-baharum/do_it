from django.shortcuts import render, get_object_or_404

# Create your views here.
from account.signals import task_evaluated
from core.models import Volunteer
from repository.models import Task
from volunteer.forms import PlayForm


def index_page(request):
    return render(request, 'volunteer/index.html')


def play_page(request):
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
    taskCount = Task.objects.filter(volunteer=volunteer, is_negative=False, is_neutral=False, is_positive=False).count()
    currentTask = Task.objects.filter(volunteer=volunteer, is_negative=False, is_neutral=False, is_positive=False)[0]
    context = {'task': currentTask, 'taskCount': taskCount}
    return render(request, 'volunteer/play.html', context)


def get_volunteer(request):
    return get_object_or_404(Volunteer, user=request.user)
