from django.dispatch import Signal, receiver

from account.models import DoerWallet

task_evaluated = Signal(providing_args=["task"])

@receiver(task_evaluated)
def task_evaluated_handler(sender, **kwargs):
    task = kwargs['task']
    wallet = DoerWallet()
    wallet.doer = task.doer
    wallet.project = task.project
    wallet.amount = task.project.task_point
    wallet.save()

