from django.db import models
from django.db.models import Q

# Create your models here.
# todo(mudzaffar):
#  class Registration
# name
# nric_no
# gender
# race
# address1
# address2
# address3
# city
# state
# birth_date
# status : REGISTERED, APPROVED, REJECTED

"""Choices"""

GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'))

RACE_CHOICES = (
    ('MALAY', 'MALAY'),
    ('CHINESE', 'CHINESE'),
    ('INDIAN', 'INDIAN'),
    ('OTHERS', 'OTHERS'),)

STATUS_REGISTRATION = (
    ('REGISTERED', 'REGISTERED'),
    ('APPROVED', 'APPROVED'),
    ('REJECTED', 'REJECTED'),)

"""State"""


class StateQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
                Q(nric_no__icontains=query) |
                Q(name__icontains=query)
        )
        return self.filter(lookup)


class StateManager(models.Manager):
    def get_queryset(self):
        return StateQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class State(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = StateManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "States"

    def get_absolute_url(self):
        return f"/portfolio/states/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""City"""


class CityQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
                Q(nric_no__icontains=query) |
                Q(name__icontains=query)
        )
        return self.filter(lookup)


class CityManager(models.Manager):
    def get_queryset(self):
        return CityQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class City(models.Model):
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False, unique=True)
    name = models.CharField(max_length=120)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = CityManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Cities"

    def get_absolute_url(self):
        return f"/portfolio/citys/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.code}:{self.name}"


"""USER """


class UserQuerySet(models.QuerySet):
    def registered(self):
        return self

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class User(models.Model):
    # id = models.IntegerField() # pk
    # creator    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    nric_no = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    nick_name = models.CharField(max_length=60, blank=False)
    address1 = models.CharField(max_length=120, blank=False)
    address2 = models.CharField(max_length=120, blank=False)
    address3 = models.CharField(max_length=120, blank=True)
    birth_date = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    race = models.CharField(max_length=60, choices=RACE_CHOICES)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Users"

    def get_absolute_url(self):
        return f"/portfolio/users/{self.nric_no}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return f"{self.name} ({self.nric_no})"
