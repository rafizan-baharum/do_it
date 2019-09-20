import json
from random import randint

from django.core.files.storage import DefaultStorage
from django.dispatch import Signal, receiver

from core.models import Volunteer
from repository.models import Task, Participant

project_created = Signal(providing_args=["project"])
project_delegated = Signal(providing_args=["project"])


@receiver(project_created)
def project_created_handler(sender, **kwargs):
    project = kwargs['project']
    # parse json
    # with open(project.repository.path, 'r') as f:
    #     parsed_json = json.load(f)
    #     for entry in parsed_json:
    #         print(entry)


@receiver(project_delegated)
def project_delegated_handler(sender, **kwargs):
    project = kwargs['project']
    # parse csv
    # create task
    # randomize task to participants
    countVolunteer = Volunteer.objects.count()
    print(countVolunteer)
    with open(project.repository.path, 'r') as f:
        parsed_json = json.load(f)
        for entry in parsed_json:
            random_volunteer = randint(0, countVolunteer - 1)
            task = Task()
            task.project = project
            task.volunteer = Volunteer.objects.all()[random_volunteer]
            task.data = entry
            task.save()

