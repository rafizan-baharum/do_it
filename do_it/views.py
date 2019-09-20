from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def index_page(request):
    return redirect('/accounts/login')

@login_required
def home_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('staff:home')
        elif request.user.is_volunteer:
            return redirect('volunteer:home')
        else:
            return render(request, 'home.html', {})
    else:
        return redirect('/accounts/login')
