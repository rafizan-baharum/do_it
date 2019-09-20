from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from account.models import VolunteerWallet
from repository.models import Project
from repository.signals import project_created, project_delegated
from staff.forms import ProjectModelForm


def index_page(request):
    earnings = VolunteerWallet.objects.filter() \
        .values('volunteer') \
        .annotate(total=Sum('amount')) \
        .order_by('-total')
    context = {'earnings': earnings}
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
