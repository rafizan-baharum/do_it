from django.contrib import admin
from django.urls import path, include

from doer.views import index_page, play_page

urlpatterns = [
    path('', index_page),
    path('home', index_page, name='home'),
    path('tasks/play', play_page, name='play'),
]
