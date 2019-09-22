from django.contrib import admin
from django.urls import path, include

from signup.views import registration_create_page

urlpatterns = [

    path('register', registration_create_page),

]
