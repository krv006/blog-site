from django.shortcuts import render
from .models import Blog , Work , About
# from .models import Work
# Create your views here.

def index(request):
    titles = Blog.objects.all()

    context = {
        'titles' : titles,
 
    }
    return render(request,'index.html',context)


def about_detail (request):
    infos = About.objects.all()
    context = {
        'infos' : infos,
    }
    return render(request,'about_html',context)

def all_blog (request):
    work_all = Work.objects.all()
    context = {
        'work_all' : work_all,
    }
    return render(request , 'all_works.html' , context)

def blog_detail (request , blog_id):
    month = Blog.objects.filter( id = blog_id)
    # infos = Work.objects.filter( id = work_id)
    images = Blog.objects.all()
    context = {
        # 'infos' : infos,
        'images' : images,
        'month' : month,
    }
    return render(request,'work_html',context)
 