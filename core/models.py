from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


"""Choices"""

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'))

RACE_CHOICES = (
    ('MALAY', 'MALAY'),
    ('CHINESE', 'CHINESE'),
    ('INDIAN', 'INDIAN'),
    ('OTHERS', 'OTHERS'),)

STATUS_CHOICES = (
    ('REGISTERED', 'REGISTERED'),
    ('APPROVED', 'APPROVED'),
    ('REJECTED', 'REJECTED'),)

INCOME_CHOICES = (
    ('B40', 'ANTARA 1000-4000 SEBULAN'),
    ('M40', 'ANTARA 4000-9000 SEBULAN'),)


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

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.code}:{self.name}"


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
    email = models.EmailField(max_length=60, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True, )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    race = models.CharField(max_length=60, choices=RACE_CHOICES, null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    income = models.CharField(max_length=60, choices=INCOME_CHOICES, default=INCOME_CHOICES[0][0], null=True)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nric_no = models.CharField(max_length=120)
    name = models.CharField(max_length=120)


class Info(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"
