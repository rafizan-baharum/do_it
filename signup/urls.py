from django.contrib import admin
from django.urls import path, include

from signup.views import registration_create_view

urlpatterns = [

    path('register', registration_create_view),

]
