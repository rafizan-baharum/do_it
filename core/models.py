from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class State(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.code}:{self.name}"


class City(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

# todo(hafiz): link with Doer
# todo(hafiz): figure out how to level-up doer
class Level(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    daily_task_count = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_doer = models.BooleanField(default=False)


class Doer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=120)
    nric_no = models.CharField(max_length=120)
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)
    #  todo(mudzaffar): city - foreignkey City
    # todo(mudzaffar): state - foreignkey State

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nric_no = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
