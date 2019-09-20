from django.contrib import admin

# Register your models here.
from repository.models import Project, Task, Vendor

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Vendor)