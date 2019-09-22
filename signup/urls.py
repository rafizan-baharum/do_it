from django.urls import path

from signup.views import registration_create_page

urlpatterns = [
    path('register', registration_create_page),
]
