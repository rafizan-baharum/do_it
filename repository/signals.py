import json
from random import randint

from django.dispatch import Signal, receiver

from core.models import Doer
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
    with open(project.repository.path, 'r') as f:
        parsed_json = json.load(f)
        for entry in parsed_json:
            print(entry)
            task = Task()
            task.project = project
            task.volunteer = recommend_random_volunteer()
            task.data = entry
            task.save()


def recommend_random_volunteer():
    count_volunteer = Doer.objects.count()
    random_volunteer = randint(0, count_volunteer - 1)
    return Doer.objects.all()[random_volunteer]


# todo(hafiz): recommendation engine based on data from data.gov
def recommend_volunteer_from_area():
    pass


# todo(alif): recommendation engine based on project tags
def recommend_volunteer_from_area(project):
    # project.tags
    # feed into recommendation engine
    pass
