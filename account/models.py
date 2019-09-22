from django.db import models

# Create your models here.
from core.models import Doer
from repository.models import Project

STATUS_CHOICES = (
    ('REQUESTED', 'REQUESTED'),
    ('APPROVED', 'APPROVED'),
    ('DECLINED', 'DECLINED'),)


class DoerWallet(models.Model):
    doer = models.ForeignKey(Doer, null=True, on_delete=models.SET_NULL, related_name='doer_wallets')
    project = models.ForeignKey( Project, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    # todo: points not amount

class Withdrawal(models.Model):
    doer = models.ForeignKey(Doer, null=True, on_delete=models.SET_NULL, related_name='doer_withdrawals')
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    withdraw_date = models.DateField(null=True, blank=True,)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
