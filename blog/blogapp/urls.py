from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/<int:about_id>', about_detail, name="about_detail"),
    path('work/<int:work_id>', work_detail, name="work_detail"), 
]