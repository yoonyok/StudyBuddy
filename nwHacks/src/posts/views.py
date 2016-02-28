from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone

def posts_home(request):
    posts = Post.objects.all()
    # search
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(course__icontains=query)
        ).distinct()

    for post in posts:
        if post.end_time < timezone.now():
            post.delete()

    context_dict = {"posts": posts, "query": query}
    return render(request, "base.html", context_dict)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "post success")
        return redirect('..')

    context_dict = {
        "form": form,
    }
    return render(request, "post_create.html", context_dict)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context_dict = {"post": post}
    return render(request, "post_detail.html", context_dict)

def post_modify(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('..')
    context_dict = {
        "form": form,
        "post": post,
    }
    return render(request, "post_create.html", context_dict)

def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "post deleted")
    return redirect("../..")

