from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


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
    allPosts = []

    allLats = []
    for post in posts:
        allLats.append(post.lat)
    post_lats = json.dumps(allLats)

    allLongs = []
    for post in posts:
        allLongs.append(post.lon)
    post_longs = json.dumps(allLongs)

    allInfo = []
    for post in posts:
        allInfo.append("Title: " + post.title + "Location: " + post.address )
    post_info = json.dumps(allInfo)

    context_dict = {"posts": posts, "post_lats": post_lats, "post_longs": post_longs, "query": query, "post_info": post_info}
    return render(request, "base.html", context_dict)


def post_create(request):
    if not request.user.is_authenticated():
        return redirect('/posts/login')
    form = PostForm(request.POST or None)
    if "cancel" in request.POST:
        return redirect('..')
    if form.is_valid():
        temp_form = form.save(commit=False)
        temp_form.user = request.user
        temp_form.save()
        # messages.success(request, "post success")
        return redirect('..')


    context_dict = {
        "form": form,
    }
    return render(request, "post_create.html", context_dict)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    context_dict = {
        "post": post,
        'comments': comments,
        "post_info":
            "Title: " + post.title + "Location: " + post.address
    }


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

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)

    if "cancel" in request.POST:
        return redirect('..')

    if form.is_valid():
        comment = Comment()
        comment.content = form.cleaned_data['content']
        comment.timestamp = datetime.now()
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('..')

    context_dict = {'form':form}

    return render(request, "comment_create.html", context_dict)


def attend(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.attendees = post.attendees + 1
    post.save()
    return redirect('../..')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if "cancel" in request.POST:
            return redirect('..')
        if form.is_valid():

            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('..')
    else:
        form = UserCreationForm()

    context_dict = {
        'form': form,
    }

    return render(request, 'register.html', context_dict)
