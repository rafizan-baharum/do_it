from django.db import models

# Create your models here.
from django.db.models import Q

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

DISTRIBUTION_CHOICES = (
    ('RANDOM', 'RANDOM'),
    ('ROUNDROBIN', 'ROUNDROBIN'),
    ('RECOMMENDATION', 'RECOMMENDATION'),
    ('AI', 'AI'),
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
    distribution = models.CharField(max_length=20, choices=DISTRIBUTION_CHOICES, default=DISTRIBUTION_CHOICES[0][0])
    task_point = models.IntegerField(default=0)

    @property
    def task_count(self):
        return Task.objects.filter(project=self).count()

    @property
    def task_count_not_done(self):
        return Task.objects.filter(
            Q(project=self) & Q(is_negative=False) & Q(is_neutral=False) & Q(is_positive=False)).count()

    @property
    def task_count_done(self):
        return Task.objects.filter(
            Q(project=self) & (Q(is_negative=True) | Q(is_neutral=True) | Q(is_positive=True))).count()


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
