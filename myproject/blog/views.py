from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

def blog_list(request):
    blogs = BlogPost.objects.all()
    return HttpResponse(blogs)