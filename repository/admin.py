from django.contrib import admin

# Register your models here.
from repository.models import Project, Participant, Task, Vendor

admin.site.register(Project)
admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(Vendor)