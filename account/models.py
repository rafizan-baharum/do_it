from django.db import models

# Create your models here.
from core.models import Doer
from repository.models import Project


class DoerWallet(models.Model):
    doer = models.ForeignKey(Doer, null=True, on_delete=models.SET_NULL, related_name='doer_wallets')
    project = models.ForeignKey( Project, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

# Model keeping track of level
