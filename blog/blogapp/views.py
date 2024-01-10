from django.shortcuts import render
from .models import Blog
from .models import About
from .models import Work
# from .models import Work
# Create your views here.

def index(request):
    titles = Blog.objects.all()
    infos = Blog.objects.all()
    images = Blog.objects.all()
    context = {
        'titles' : titles,
        'infos' : infos,
        'images': images,
    }
    return render(request,'index.html',context)


def about_detail (request):
    infos = About.objects.all()
    context = {
        'infos' : infos,
    }
    return render(request,'about_html',context)

def all_works (request):
    work_all = Work.objects.all()
    context = {
        'work_all' : work_all,
    }
    return render(request , 'all_works.html' , context)

def work_detail (request , work_id):
    month = Work.objects.filter( id = work_id)
    infos = Work.objects.filter( id = work_id)
    images = Work.objects.all()
    context = {
        'infos' : infos,
        'images' : images,
        'month' : month,
    }
    return render(request,'work_html',context)
 