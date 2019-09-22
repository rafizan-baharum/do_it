from django.shortcuts import render, redirect

# Create your views here.
from signup.forms import RegistrationModelForm
from signup.models import Registration
from signup.signals import registration_approved


def registration_create_page(request):
    form = RegistrationModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        context = {'registration': obj}
        return render(request, 'signup/confirmation.html', context)
    return render(request, 'signup/register.html', context)
