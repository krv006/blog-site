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


def about_detail (request , about_id ):
    infos = Blog.objects.filter( id = about_id)
    images = About.objects.all()
    context = {
        'infos' : infos,
        'images' : images,
    }
    return render(request,'about_html',context)



def work_detail (request , work_id):
    infos = Work.objects.filter( id = work_id)
    images = Work.objects.all()
    context = {
        'infos' : infos,
        'images' : images,
    }
    return render(request,'work_html',context)
 