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
from core.models import City, State, GENDER_CHOICES, RACE_CHOICES, INCOME_CHOICES, STATUS_CHOICES

"""REGISTRATION """


class RegistrationQuerySet(models.QuerySet):
    def registered(self):
        return self

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)


class RegistrationManager(models.Manager):
    def get_queryset(self):
        return RegistrationQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class Registration(models.Model):
    # id = models.IntegerField() # pk
    nric_no = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=1000, null=False)
    address1 = models.CharField(max_length=120, blank=False, null=True)
    address2 = models.CharField(max_length=120, blank=False, null=True)
    address3 = models.CharField(max_length=120, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True,)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    race = models.CharField(max_length=60, choices=RACE_CHOICES, null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    income = models.CharField(max_length=60, choices=INCOME_CHOICES, default=INCOME_CHOICES[0][0], null=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = RegistrationManager()

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = "Registrations"
