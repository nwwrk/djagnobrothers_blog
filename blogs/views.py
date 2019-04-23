from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    context = {
        'title': 'Blog Site',
        'msg': 'Here is a top page.',
        'blg': blogs,
    }

    return render(request, 'blogs/index.html', context)

def detail(request, blog_id):
    blog =Blog.objects.get(id=blog_id)
    context = {
        'title': 'Blog Application',
        'blg': blog,
    }
    return render(request, 'blogs/detail.html', context)
