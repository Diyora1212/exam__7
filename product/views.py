from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.views.decorators.http import require_http_methods
from .models import *


def home(request):
    # data = TestCard.objects.all()
    return render(request, template_name='index.html')


def explore(request):
    # data = TestCard.objects.all()
    return render(request, template_name='explore.html')


def detail_view(request):
    # data = TestCard.objects.all()
    return render(request, template_name='details.html')


@login_required
def create_view(request):
    # data = TestCard.objects.all()
    return render(request, template_name='create.html')


def author_view(request, author_id):
    model = ProductAuthor
    author = ProductAuthor.objects.get(pk=author_id)
    like_count = author.calculate_like_count()

    context = {
        'like_count': like_count,
    }

    return render(request, template_name='author.html', context=context)


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You have logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form submission. Please check your data.")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "login.html", context=context)


@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == "POST":
        create_form = UserRegisterForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Invalid form submission. Please check your data.")
    else:
        create_form = UserRegisterForm()

    context = {
        "form": create_form
    }
    return render(request, "register.html", context=context)


@require_http_methods(["GET"])
def logout(request):
    logout(request)
    messages.success(request, "User successfully logged out")
    return redirect("home")
