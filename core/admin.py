from django.contrib import admin

# Register your models here.
from core.models import Volunteer, Staff, User

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Volunteer)