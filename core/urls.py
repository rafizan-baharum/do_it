from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.base_info, name='base_info'),
]