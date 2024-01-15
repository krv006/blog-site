from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    
    path('', index),
    path('about/', about, name="about"),
    
    
    path('blogs/', all_blog, name="all_blog"),#
    path('blog/<int:blog_id>', blog_detail , name="blog_detail"), #
    
    
    path('work/<int:work_id>', work_detail , name="work_detail"),  
    path('work/', work, name="work"),
   
    
]