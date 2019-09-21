from django.contrib import admin
from django.urls import path, include

from signup.views import user_create_view

urlpatterns = [

path('register',user_create_view),

]
