from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return HttpResponse("Welcome to the Blog!")