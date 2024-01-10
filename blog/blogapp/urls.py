from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about_detail, name="about_detail"),
    path('works/', work_detail, name="work_detail"),
    path('work/<int:work_id>', work_detail, name="work_detail"),

]