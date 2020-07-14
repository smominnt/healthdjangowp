from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
from .models import User
from .forms import CreateUserForm


def register_view(request):
    if request.user.is_authenticated:   # redirect to home if the user is already logged in
        return redirect('..')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user)

                return redirect('..')  # redirect to login page
        context = {'form': form}
        return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated: # redirect to home if the user is already logged in
        return redirect('..')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('..')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('accounts:login')