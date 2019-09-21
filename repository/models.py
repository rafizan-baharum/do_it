from django.db import models

# Create your models here.
from core.models import Doer

TYPE_CHOICES = (
    ('GLC', 'GLC'),
    ('MNC', 'MNC'),
    ('GOVERNMENT', 'GOVERNMENT'),
    ('NGO', 'NGO'),
)

STATUS_CHOICES = (
    ('DRAFTED', 'DRAFTED'),
    ('DELEGATED', 'DELEGATED'),
    ('COMPLETED', 'COMPLETED'),
)


class Vendor(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])

    def __str__(self):
        return f"{self.pk}:{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=120)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL, related_name='projects')
    repository = models.FileField(blank=True, null=True)  # data
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    task_point = models.IntegerField(default=0)


class Task(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, related_name='project_tasks')
    data = models.CharField(max_length=120)
    doer = models.ForeignKey(Doer, null=True, on_delete=models.SET_NULL)

    is_negative = models.BooleanField(default=False)
    is_positive = models.BooleanField(default=False)
    is_neutral = models.BooleanField(default=False)

    @property
    def is_completed(self):
        return self.is_negative | self.is_positive | self.is_positive
