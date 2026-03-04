from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'a_post/post_add.html', {'form': form, 'title': 'Add New Post'})


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
            messages.info(request, "Comment submitted and awaiting approval.")
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'a_post/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.is_approved = False  # Re-verify after edit
            post.save()
            messages.success(request, "Post updated and sent for re-approval!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'a_post/post_add.html', {
        'form': form, 
        'post': post,
        'edit_mode': True,  # Flag to indicate we're in edit mode
        })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post successfully deleted.")
        return redirect('home')
    return redirect('post_detail', pk=pk)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    post_pk = comment.post.pk
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.is_approved = False # Require re-approval
            comment.save()
            messages.success(request, "Comment updated and sent for re-approval!")
        
    return redirect('post_detail', pk=post_pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    post_pk = comment.post.pk
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment successfully deleted.")
    return redirect('post_detail', pk=post_pk)