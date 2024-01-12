from django.shortcuts import render
from .models import Blog , Work , About
# from django .template.loader import render_to_string 
# Create your views here.

def index(request):
    titles = Blog.objects.all()
    # response = render_to_string ('templates/index.html')
    context = {
        'titles' : titles,
        # 'response' : response ,
    }
    return render(request,'index.html',context)


def about_detail (request):
    infos = About.objects.all()
    context = {
        'infos' : infos,
    }
    return render(request,'about.html',context)

def all_blog (request):
    work_all = Work.objects.all()
    context = {
        'work_all' : work_all,
    }
    return render(request , 'all_works.html' , context)

def blog_detail (request , blog_id):
    month = Blog.objects.filter( id = blog_id)
    images = Blog.objects.all()
    # infos = Work.objects.filter( id = work_id)
    context = {
        'images' : images,
        'month' : month,
        # 'infos' : infos,
    }
    return render(request,'work.html',context)
 