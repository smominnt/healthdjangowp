from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm

from .models import Post
# Create your views here.

@login_required(login_url='accounts:login')
def posts_view(request): # display all posts in database
    queryset = Post.objects.all()
    context = {
        "list":queryset
    }
    return render(request, "posts.html", context)

@login_required(login_url='accounts:login')
def posts_detail_view(request, id=None): # display a specific post and it's contents
    list = Post.objects.all()
    obj = get_object_or_404(Post, id=id)
    pos = 0
    while pos < len(list) and list[pos].id != obj.id:
        pos += 1
    prev, nxt = None, None
    if pos > 0:
        prev = list[pos - 1]
    if pos < len(list) - 1:
        nxt = list[pos + 1]
    list = [prev, obj, nxt] # save access to next and previous posts by creation id
    if not Post:
        return posts_view(request)
    context = {
        "obj": obj,
        "pos": pos,
        "list": list
    }
    return render(request, "posts_detail.html", context)

@login_required(login_url='accounts:login')
def posts_create_view(request): # display page to create a post
    my_form = PostForm(request.POST or None)
    if my_form.is_valid():
        instance = my_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/posts/' + str(instance.id))
    context = {
        'form': my_form
    }
    return render(request, "posts_create.html", context)

@login_required(login_url='accounts:login')
def posts_edit_view(request, id=id): # display page to edit a post
    obj = get_object_or_404(Post, id=id)
    if obj.user != request.user: # if the currently logged in user isn't the author, edit permission is restricted
        return HttpResponseForbidden()
    my_form = PostForm(request.POST or None, instance=obj)

    if request.POST and my_form.is_valid():
        my_form.save()
        return redirect('/posts/' + str(id))
    context = {
        'form': my_form,
        "title": obj.title,
        "content": obj.content,
    }
    return render(request, "posts_edit.html", context)

@login_required(login_url='accounts:login')
def posts_delete_view(request, id):
    obj = get_object_or_404(Post, id=id)
    if obj.user != request.user:  # if the currently logged in user isn't the author, edit permission is restricted
        return HttpResponseForbidden()
    if request.method == "POST":
        obj.delete()
        return redirect('..')
    context = {
        "obj":obj
    }
    return render(request, "posts_delete.html", context)
