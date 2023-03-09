from time import sleep
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .form import LoginForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'نام کاربری یا رمز عبور صحیح نمیباشد')
                return redirect(reverse("account:login"))
            login(request, user)
            return redirect(reverse('system:home'))
    else:
        if request.user.is_authenticated:
            return redirect('system:home')
        user_form = LoginForm()
    return render(request, 'index.html', {'form': user_form})

