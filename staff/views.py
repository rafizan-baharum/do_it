from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

# Create your views here.
from account.models import VolunteerWallet
from core.models import Volunteer
from repository.models import Project
from repository.signals import project_created, project_delegated
from staff.forms import ProjectModelForm


def index_page(request):
    projects = Project.objects.all()
    volunteer_earnings = Volunteer.objects.all()\
        .annotate(total=Coalesce(Sum('volunteer_wallets__amount'), 0))\
        .order_by('-total')
    for volunteer_earning in volunteer_earnings:
        print(dir(volunteer_earning))
    context = {
        'projects': projects,
        'volunteer_earnings': volunteer_earnings
    }
    return render(request, 'staff/index.html', context)


def project_list_page(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'staff/project_list.html', context)


def project_detail_page(request, pk):
    project = Project.objects.filter(pk=pk).first()
    context = {'project': project}
    return render(request, 'staff/project_detail.html', context)


def project_create_page(request):
    form = ProjectModelForm(request.POST, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        project_created.send(sender=None, project=obj)
        return redirect('staff:home')
    else:
        context = {'form': form}
        return render(request, 'staff/project_create.html', context)


def project_delegate_page(request, pk):
    project = Project.objects.filter(pk=pk).first()
    Project.objects.filter(pk=pk).update(status='DELEGATED')
    project_delegated.send(sender=None, project=project)
    return redirect('staff:project_detail', pk=pk)


# todo(mudzaffar):
def level_list_page(request):
    pass


# todo(mudzaffar):
def level_detail_page(request, pk):
    pass


# todo(mudzaffar):
def level_update_page(request, pk):
    pass
