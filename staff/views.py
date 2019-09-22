from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

# Create your views here.
from account.models import DoerWallet
from core.models import Doer
from repository.models import Project, Vendor
from repository.signals import project_created, project_delegated
from signup.models import Registration
from staff.forms import ProjectModelForm, VendorModelForm


def index_page(request):
    projects = Project.objects.all()
    doer_earnings = Doer.objects.all() \
        .annotate(total=Coalesce(Sum('doer_wallets__amount'), 0)) \
        .order_by('-total')
    context = {
        'projects': projects,
        'doer_earnings': doer_earnings
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
    form = ProjectModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        project_created.send(sender=None, project=obj)
        return redirect('staff:home')
    else:
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


# todo(mudzaffar):
def doer_list_page(request):
    pass


# todo(mudzaffar):
def doer_detail_page(request, pk):
    pass


# todo(mudzaffar):
def doer_update_page(request, pk):
    pass

# todo(mudzaffar):
def registration_list_page(request):
    registrations = Registration.objects.all()
    context = {'registrations': registrations}
    return render(request, 'staff/registration_list.html', context)


# todo(mudzaffar):
def registration_detail_page(request, pk):
    registration = Registration.objects.filter(pk=pk).first()
    context = {'registration': registration}
    return render(request, 'staff/registration_detail.html', context)

def registration_approve_page(request, pk):
    Registration.objects.filter(pk=pk).update(status='APPROVED')
    return redirect('staff:registration_detail', pk=pk)


# todo(mudzaffar):
def registration_update_page(request, pk):
    pass


# todo(mudzaffar):
def vendor_list_page(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'staff/vendor_list.html', context)


def vendor_detail_page(request, pk):
    vendor = Vendor.objects.filter(pk=pk).first()
    context = {'vendor': vendor}
    return render(request, 'staff/vendor_detail.html', context)


def vendor_create_page(request):
    form = VendorModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        # signal??
        return redirect('staff:vendor_list')
    else:
        return render(request, 'staff/vendor_create.html', context)

def vendor_update_page(request, pk):
    pass
