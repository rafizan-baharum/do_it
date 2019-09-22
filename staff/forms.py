from django import forms

from repository.models import Project, Vendor


class VendorModelForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'type']


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'vendor', 'distribution', 'repository', 'task_point']
