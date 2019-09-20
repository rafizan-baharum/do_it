from django.db import models

# Create your models here.
from core.models import Volunteer
from repository.models import Project


class VolunteerWallet(models.Model):
    volunteer = models.ForeignKey( Volunteer, null=True, on_delete=models.SET_NULL, related_name='repositories')
    project = models.ForeignKey( Project, null=True, on_delete=models.SET_NULL, related_name='repositories')
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
