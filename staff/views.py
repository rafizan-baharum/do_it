from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect

# Create your views here.
from account.models import DoerWallet, Withdrawal
from account.signals import withdrawal_approved
from core.models import Doer
from repository.models import Project, Vendor, Task
from repository.signals import project_created, project_delegated
from signup.models import Registration
from signup.signals import registration_approved
from staff.forms import ProjectModelForm, VendorModelForm


def index_page(request):
    projects = Project.objects.all()
    doer_earnings = Doer.objects.all() \
        .annotate(total=Coalesce(Sum('doer_wallets__amount'), 0)) \
        .order_by('-total')
    context = {
        'projects': projects,
        'doer_earnings': doer_earnings,
        'current_user': request.user,
    }
    return render(request, 'staff/index.html', context)


def project_list_page(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'current_user': request.user
    }
    return render(request, 'staff/project_list.html', context)


def project_detail_page(request, pk):
    project = Project.objects.filter(pk=pk).first()
    context = {
        'project': project,
        'current_user': request.user,
        'doer_tasks': Task.objects.filter(project_id=pk).select_related('doer').all()
    }
    return render(request, 'staff/project_detail.html', context)


def project_create_page(request):
    form = ProjectModelForm(request.POST or None, request.FILES or None)
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


def doer_list_page(request):
    doers = Doer.objects.all()
    context = {'doers': doers}
    return render(request, 'staff/doer_list.html', context)


def doer_detail_page(request, pk):
    doer = Doer.objects.filter(pk=pk).first()
    context = {'doer': doer}
    return render(request, 'staff/doer_detail.html', context)


def doer_update_page(request, pk):
    pass


def registration_list_page(request):
    registrations = Registration.objects.filter(status='REGISTERED').all()
    context = {
        'registrations': registrations,
        'current_user': request.user,
    }
    return render(request, 'staff/registration_list.html', context)


def registration_detail_page(request, pk):
    registration = Registration.objects.filter(pk=pk).first()
    context = {
        'registration': registration,
        'current_user': request.user
    }
    return render(request, 'staff/registration_detail.html', context)


def registration_approve_page(request, pk):
    Registration.objects.filter(pk=pk).update(status='APPROVED')
    return redirect('staff:registration_detail', pk=pk)


# todo(mudzaffar):
def registration_update_page(request, pk):
    pass


def vendor_list_page(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
        'current_user': request.user
    }
    return render(request, 'staff/vendor_list.html', context)


def vendor_detail_page(request, pk):
    vendor = Vendor.objects.filter(pk=pk).first()
    context = {
        'vendor': vendor,
        'current_user': request.user
    }
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


def withdrawal_list_page(request):
    withdrawals = Withdrawal.objects.all()
    context = {
        'withdrawals': withdrawals,
        'current_user': request.user,
    }
    return render(request, 'staff/withdrawal_list.html', context)


def withdrawal_detail_page(request, pk):
    withdrawal = Withdrawal.objects.filter(pk=pk).first()
    context = {
        'withdrawal': withdrawal,
        'current_user': request.user
    }
    return render(request, 'staff/withdrawal_detail.html', context)


def withdrawal_approve_page(request, pk):
    withdrawal = Withdrawal.objects.filter(pk=pk).first()
    Withdrawal.objects.filter(pk=pk).update(status='APPROVED')
    withdrawal_approved.send(sender=None, withdrawal=withdrawal)
    return redirect('staff:withdrawal_list')


def withdrawal_decline_page(request, pk):
    Withdrawal.objects.filter(pk=pk).update(status='DECLINED')
    return redirect('staff:withdrawal_list')


def registration_approve_page(request, pk):
    registration = Registration.objects.filter(pk=pk).first()
    Registration.objects.filter(pk=pk).update(status='APPROVED')
    registration_approved.send(sender=None, registration=registration)
    return redirect('staff:registration_list')


def registration_decline_page(request, pk):
    Registration.objects.filter(pk=pk).update(status='DECLINED')
    return redirect('staff:registration_list')
