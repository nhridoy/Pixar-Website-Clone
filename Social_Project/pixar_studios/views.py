from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from pixar_studios.models import DisneyPlusBlogs, TheatricalShorts, WebSites, UserInfo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# Decorator
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


def home(request):
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        users = UserInfo.objects.get(user=user.id)
        data = {
            'title': 'Pixar Studios',
            'users': users,
        }
    else:
        data = {
            'title': 'Pixar Studios',
        }

    return render(request, 'pixar_studios/index.html', context=data)


@login_required
def disneyplus(request):
    disneyplusall = DisneyPlusBlogs.objects.all()
    data = {
        'title': 'Disney Plus',
        'disneyplusall': disneyplusall,
    }

    return render(request, 'pixar_studios/disneyplus.html', context=data)


@login_required
def theatricalshorts(request):
    theatricalshortsall = TheatricalShorts.objects.all()
    data = {
        'title': 'Theatrical Shorts',
        'theatricalshortsall': theatricalshortsall,
    }

    return render(request, 'pixar_studios/theatrical-shorts.html', context=data)


@login_required
def featurefilms(request):
    data = {}

    return render(request, 'pixar_studios/feature-films.html', context=data)


@login_required
def theatricalshort(request, theatrical_id):
    short = TheatricalShorts.objects.get(shorts_title=theatrical_id)
    data = {
        'title': theatrical_id,
        'short': short,
    }

    return render(request, 'pixar_studios/theatrical-short.html', context=data)


@login_executed('pixar_studios:home')
def registration(request):
    registered = False

    if request.method == 'POST':
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        username = request.POST["user-name"]
        password = request.POST["password"]
        facebook_id = request.POST["fb-link"]
        bio = request.POST["bio"]

        user = User()
        user_info = UserInfo()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.password = password
        user.save()
        user.set_password(user.password)
        user.save()

        user_info.user = user
        if 'image' in request.FILES:
            profile_pic = request.FILES["image"]
            user_info.profile_pic = profile_pic
        user_info.facebook = facebook_id
        user_info.bio = bio
        user_info.save()

        registered = True
        login_page(request)
        return HttpResponseRedirect(reverse('pixar_studios:home'))

    data = {
        'title': 'Registration',
    }

    return render(request, 'pixar_studios/registration.html', context=data)


@login_executed('pixar_studios:home')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user-name')
        password = request.POST.get('password')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                # print("Login Ok")
                return HttpResponseRedirect(reverse('pixar_studios:home'))
            else:
                print("Account not active")
        else:
            print("Login Details Wrong")

    data = {
        'title': 'Login',
    }

    return render(request, 'pixar_studios/login_page.html', context=data)


@login_required
def logout_url(request):
    logout(request)
    return HttpResponseRedirect(reverse('pixar_studios:home'))


@login_required
def profile_url(request, user_name):
    user = User.objects.get(username=user_name)
    users = UserInfo.objects.get(user=user.id)

    data = {
        'title': f'{user.first_name} {user.last_name}',
        'users': users,

    }
    return render(request, 'pixar_studios/profile.html', context=data)
