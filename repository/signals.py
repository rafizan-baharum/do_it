from random import randint

from django.dispatch import Signal, receiver

from repository.models import Task, Participant

project_delegated = Signal(providing_args=["project"])


@receiver(project_delegated)
def project_delegated_handler(sender, **kwargs):
    project = kwargs['project']
    # parse csv
    # create task
    # randomize task to participants
    countParticipant = Participant.objects.filter(project=project)
    for i in range(10):  # for example
        random_index = randint(0, countParticipant - 1)
        task = Task()
        task.project = project
        task.volunteer = Participant.objects.all()[random_index]
        task.data = 'Some Data'
        task.save()
