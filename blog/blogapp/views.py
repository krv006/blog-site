from django.shortcuts import render
from .models import Blog , Work , About
#about ni qoshish 

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


def work (request ):
    work = Work.objects.all()
    context = {
        'work' : work
    }
    return render(request,'work.html',context)


def work_detail(request, work_id):
    work = Work.objects.filter(id=work_id)
    context = {
        'work' : work,
    }
    return render (request , 'work_detail.html', context)