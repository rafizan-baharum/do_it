from django.dispatch import Signal, receiver

from account.models import DoerWallet

task_evaluated = Signal(providing_args=["task"])
withdrawal_approved = Signal(providing_args=["withdrawal"])


@receiver(task_evaluated)
def task_evaluated_handler(sender, **kwargs):
    task = kwargs['task']
    wallet = DoerWallet()
    wallet.doer = task.doer
    wallet.project = task.project
    wallet.point = task.project.task_point
    wallet.save()


@receiver(withdrawal_approved)
def withdrawal_approved_handler(sender, **kwargs):
    withdrawal = kwargs['withdrawal']
    wallet = DoerWallet()
    wallet.doer = withdrawal.doer
    wallet.project = None
    wallet.point = withdrawal.amount * -1
    wallet.save()
