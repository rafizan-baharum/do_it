from django.urls import path

from staff.views import index_page, project_list_page, project_detail_page, project_create_page, project_delegate_page, \
    level_detail_page, level_list_page, level_update_page, vendor_list_page, vendor_create_page, vendor_detail_page, \
    vendor_update_page, registration_list_page, registration_detail_page, registration_update_page, \
    registration_approve_page, doer_list_page, doer_detail_page, doer_update_page, withdrawal_list_page, \
    withdrawal_detail_page, withdrawal_approve_page, withdrawal_decline_page, registration_decline_page

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
    path('vendors/list/', vendor_list_page, name='vendor_list'),
    path('vendors/create/', vendor_create_page, name='vendor_create'),
    path('vendors/<str:pk>/', vendor_detail_page, name='vendor_detail'),
    path('vendors/<str:pk>/update/', vendor_update_page, name='vendor_update'),
    path('doers/list/', doer_list_page, name='doer_list'),
    path('doers/<str:pk>/', doer_detail_page, name='doer_detail'),
    path('doers/<str:pk>/update/', doer_update_page, name='doer_update'),
    path('registrations/list/', registration_list_page, name='registration_list'),
    path('registrations/<str:pk>/', registration_detail_page, name='registration_detail'),
    path('registrations/<str:pk>/update/', registration_update_page, name='registration_update'),
    path('registrations/<str:pk>/approve/', registration_approve_page, name='registration_approve'),
    path('registrations/<str:pk>/decline/', registration_decline_page, name='registration_decline'),
    path('withdrawals/list/', withdrawal_list_page, name='withdrawal_list'),
    path('withdrawals/<str:pk>/', withdrawal_detail_page, name='withdrawal_detail'),
    path('withdrawals/<str:pk>/approve/', withdrawal_approve_page, name='withdrawal_approve'),
    path('withdrawals/<str:pk>/decline/', withdrawal_decline_page, name='withdrawal_decline'),
]
