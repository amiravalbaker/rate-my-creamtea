from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'a_post/post_list.html', {'posts': posts})


def post_detail(request, pk):
    return render(request, 'a_post/post_detail.html', {'pk': pk})


def post_add(request):
    return render(request, 'a_post/post_add.html')
