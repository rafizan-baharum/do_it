from django.urls import path

from staff.views import index_page, project_list_page, project_detail_page, project_create_page, project_delegate_page, \
    level_detail_page, level_list_page, level_update_page

urlpatterns = [
    path('', index_page),
    path('home', index_page, name='home'),
    path('projects/list/', project_list_page, name='project_list'),
    path('projects/create/', project_create_page, name='project_create'),
    path('projects/<str:pk>/', project_detail_page, name='project_detail'),
    path('projects/<str:pk>/delegate/', project_delegate_page, name='project_delegate'),
    path('levels/list/', level_list_page, name='level_list'),
    path('levels/<str:pk>/', level_detail_page, name='level_detail'),
    path('levels/<str:pk>/update/', level_update_page, name='level_update'),
]
