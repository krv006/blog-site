from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about_detail, name="about_detail"),
    path('blog/', all_blog, name="all_blog"),
    path('blog/<int:blog_id>', blog_detail , name="blog_detail"),

]