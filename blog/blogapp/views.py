from django.shortcuts import render
from .models import Blog , Work , About


def index(request):
    
    
    return render(request,'index.html')


def about (request):
    return render(request,'about.html')


def all_blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs,
    }
    return render(request , 'all_blog.html' , context)

def blog_detail (request , blog_id):
    blog = Blog.objects.filter( id = blog_id)
    context = {
        'blog' : blog,
    }
    return render(request,'blog.html',context)


def work (request):
    
    context = {
    
    }
    return render(request,'work.html',context)