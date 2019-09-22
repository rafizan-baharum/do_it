from django.contrib import admin
from django.urls import path, include

from doer.views import index_page, play_page, project_list_page

urlpatterns = [
    path('', index_page),
    path('home', index_page, name='home'),
    path('projects/list', project_list_page, name='project_list'),
    path('tasks/play/<str:pk>', play_page, name='play'),
]
