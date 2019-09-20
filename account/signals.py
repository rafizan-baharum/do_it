from django.dispatch import Signal, receiver

from account.models import VolunteerWallet

task_evaluated = Signal(providing_args=["task"])

@receiver(task_evaluated)
def task_evaluated_handler(sender, **kwargs):
    task = kwargs['task']
    wallet = VolunteerWallet()
    wallet.volunteer = task.volunteer
    wallet.project = task.project
    wallet.amount = 0.10
    wallet.save()

