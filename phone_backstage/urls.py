from django.contrib import admin
from django.urls import path, re_path,include
from .views import *


urlpatterns = [
    path('index',dx),
    path('home',home)
]