from django.urls import path

from doer.views import index_page, play_page, project_list_page, withdrawal_list_page, withdrawal_detail_page, \
    withdrawal_create_page

urlpatterns = [
    path('', index_page),
    path('home', index_page, name='home'),
    path('projects/list', project_list_page, name='project_list'),
    path('tasks/play/<str:pk>', play_page, name='play'),
    path('withdrawals/list/', withdrawal_list_page, name='withdrawal_list'),
    path('withdrawals/create/', withdrawal_create_page, name='withdrawal_create'),
    path('withdrawals/<str:pk>/', withdrawal_detail_page, name='withdrawal_detail'),
]
