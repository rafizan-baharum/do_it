from django.shortcuts import render

# Create your views here.
from signup.forms import RegistrationModelForm


def registration_create_page(request):
    form = RegistrationModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        context = {'registration': obj}
        return render(request, 'signup/confirmation.html', 'context')
    else:
        return render(request, 'signup/register.html', context)
