import json
from random import randint

from django.dispatch import Signal, receiver

from core.models import Volunteer
from repository.decorators import start_new_thread
from repository.models import Task

project_created = Signal(providing_args=["project"])
project_delegated = Signal(providing_args=["project"])


@receiver(project_created)
def project_created_handler(sender, **kwargs):
    project = kwargs['project']

@receiver(project_delegated)
def project_delegated_handler(sender, **kwargs):
    project = kwargs['project']
    # parse csv
    # create task
    # randomize task to participants
    assign_random_task(project)

@start_new_thread
def assign_random_task(project):
    countVolunteer = Volunteer.objects.count()
    with open(project.repository.path, 'r') as f:
        parsed_json = json.load(f)
        for entry in parsed_json:
            random_volunteer = randint(0, countVolunteer - 1)
            task = Task()
            task.project = project
            task.volunteer = Volunteer.objects.all()[random_volunteer]
            task.data = entry
            task.save()

