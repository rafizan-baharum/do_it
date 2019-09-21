from django import forms

from repository.models import Project


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'vendor', 'repository', 'task_point']
