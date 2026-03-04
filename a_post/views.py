from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

# give all posts so user unlogged in can see all posts, but only approved ones
# logged in can see their own unapproved posts and all approved posts


def home(request):
    posts = Post.objects.all().order_by('-created_at')
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
            return redirect('posts:home')
    else:
        form = PostForm()

    return render(request, 'a_post/post_add.html', {'form': form, 'title': 'Add New Post'})


def post_detail(request, pk):
    # removed the filter for approved posts so that users can see their own unapproved posts
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.info(request, "Comment submitted and awaiting approval.")
            return redirect('posts:post_detail', pk=post.pk)
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
            return redirect('posts:post_detail', pk=post.pk)
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
        return redirect('posts:home')
    return redirect('posts:post_detail', pk=pk)


@login_required
def comment_edit(request, post_pk, comment_pk):
    """Allows a user to edit their own comment"""
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # Only the comment author or staff can edit
    if request.user != comment.user and not request.user.is_staff:
        messages.error(request, "You can only edit your own comments.")
        return redirect('posts:post_detail', pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect('posts:post_detail', pk=post_pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'a_post/comment_form.html', {
        'form': form,
        'post': post,
        'comment': comment,
        'edit_mode': True
    })


@login_required
def comment_delete(request, post_pk, comment_pk):
    """Allows a user to delete their own comment"""
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # Only the comment author or staff can delete
    if request.user != comment.user and not request.user.is_staff:
        messages.error(request, "You can only delete your own comments.")
        return redirect('posts:post_detail', pk=post_pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
        return redirect('posts:post_detail', pk=post_pk)

    return render(request, 'a_post/comment_confirm_delete.html', {
        'post': post,
        'comment': comment
    })
