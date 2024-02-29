from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.urls import reverse
# from .forms import UserRegisterForm, UserLoginForm
from django.views.decorators.http import require_http_methods
from django.views.generic import View

from .models import *


def home(request):
    data = Product.objects.all()
    return render(request, template_name='index.html', context={'data': data})


def explore(request):
    # data = TestCard.objects.all()
    return render(request, template_name='explore.html')


def detail_view(request):
    # data = TestCard.objects.all()
    return render(request, template_name='details.html')


@login_required
def create_view(request):
    return render(request, template_name='create.html')


def author_view(request):
    # user = get_object_or_404(
    #     User.objects.annotate(total_likes=Count('post__likes')), pk=user_id
    # )
    # products = Product.objects.filter(author=user)
    # return render(
    #     request,
    #     'author.html',
    #     {'user': user, 'posts': products, 'request_user': request.user},
    # )
    return render(request, template_name='author.html')


# @login_required
# def like_author(request, author_id):
#     author = get_object_or_404(ProductAuthor, pk=author_id)
#     user = request.user
#
#     # Check if the user has already liked the author
#     if not AuthorLike.objects.filter(author=author, user=user).exists():
#         # If not, create a new like
#         AuthorLike.objects.create(author=author, user=user)
#         # Update the like count in the author model
#         author.like_count += 1
#         author.save()
#
#     # Return a JsonResponse with the updated like count
#     return JsonResponse({'like_count': author.like_count})


# @require_http_methods(["GET", "POST"])

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# @require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    messages.success(request, "User successfully logged out")
    return redirect("home")
