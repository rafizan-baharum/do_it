from django.contrib import admin
from django.urls import path, include

from volunteer.views import index_page

urlpatterns = [
    path('', index_page),
    path('home', index_page, name='home'),
]
