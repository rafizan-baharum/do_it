from django.shortcuts import render
from core.models import Info

# Create your views here.

def base_info(request):
    infos = Info.objects.all()
    context = {'infos': infos}
    return render(request, "base_info.html", context)

def map_info(request):
    return render(request, "map_info.html", {})
