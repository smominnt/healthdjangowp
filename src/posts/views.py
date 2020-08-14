from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

from .models import Post, Comment
# Create your views here.


def dislike(request, id=id):
    instance = get_object_or_404(Post, id=id)
    if (request.user in instance.downvote.all()):
        instance.downvote.remove(request.user)
    else:
        instance.downvote.add(request.user)
        instance.upvote.remove(request.user)
    return HttpResponse(status=204)

def like(request, id=id):
    instance = get_object_or_404(Post, id=id)
    if (request.user in instance.upvote.all()):
        instance.upvote.remove(request.user)
    else:
        instance.upvote.add(request.user)
        instance.downvote.remove(request.user)
    return HttpResponse(status=204)

@login_required(login_url='accounts:login')
def posts_view(request): # display all posts in database
    queryset = Post.objects.all()
    voted = []
    for x in queryset:
        if (request.user in x.upvote.all()):
            voted.append(1)
        elif (request.user in x.downvote.all()):
            voted.append(-1)
        else:
            voted.append(0)

    context = {
        "list": zip(queryset, voted),
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
    voted = 0
    if (request.user in obj.upvote.all()):
        voted = 1
    elif (request.user in obj.downvote.all()):
        voted = -1

    new_comment = None
    comments = obj.comments
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = obj
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "obj": obj,
        "pos": pos,
        "list": list,
        "voted": voted,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    }
    return render(request, "posts_detail.html", context)

@login_required(login_url='accounts:login')
def posts_create_view(request): # display page to create a post
    my_form = PostForm(request.POST or None, request.FILES or None)
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
    instance = get_object_or_404(Post, id=id)
    if instance.user != request.user: # if the currently logged in user isn't the author, edit permission is restricted
        return HttpResponseForbidden()
    my_form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if my_form.is_valid():
        instance = my_form.save(commit=False)
        instance.save()
        return redirect('/posts/' + str(id))
    context = {
        'form': my_form
    }
    return render(request, "posts_edit.html", context)

@login_required(login_url='accounts:login')
def posts_delete_view(request, id):
    obj = get_object_or_404(Post, id=id)
    if obj.user != request.user:  # if the currently logged in user isn't the author, edit permission is restricted
        return HttpResponseForbidden()
    if request.method == "POST":
        obj.delete()
        obj.file.delete()
        return redirect('..')
    context = {
        "obj":obj
    }
    return render(request, "posts_delete.html", context)
