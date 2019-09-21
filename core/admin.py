from django.contrib import admin

# Register your models here.
from core.models import Doer, Staff, User, State, City, Level

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Doer)
admin.site.register(Level)
admin.site.register(City)
admin.site.register(State)