from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def home(request):
    posts = Post.objects.filter(is_approved=True)
    return render(request, 'a_post/post_list.html', {'posts': posts})


@login_required
def post_add(request):
    """Allows a logged-in user to upload a new food post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # request.FILES is required for Cloudinary
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # Note: is_approved defaults to False in the model, 
            # so it won't show in post_list until an admin approves it.
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'a_post/post_form.html', {'form': form, 'title': 'Add New Post'})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=True)
    comments = post.comments.filter(is_approved=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'a_post/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
