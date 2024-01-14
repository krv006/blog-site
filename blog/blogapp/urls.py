from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name="about"),
    
    path('blogs/', all_blog, name="all_blog"),#
    path('blog/<int:blog_id>', blog_detail , name="blog_detail"), #
    
    
    # path('work/', all_work, name="all_work"),
    # path('work/<int:work_id>', work , name="work"), 

]