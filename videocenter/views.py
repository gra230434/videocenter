from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Hello, world. You're at the video index."
    context = {'mes': message}
    return render(request, 'index/index.html', context)


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            HttpResponseRedirect('/account/')
        else:
            HttpResponseRedirect('/login/?message=error')
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Welcome Video Center"
    context = {'message': message}
    return render(request, 'index/login.html', context)


def register_page(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Welcome register"
    context = {'message': message}
    return render(request, 'index/register.html', context)


def logout_action(request):
    logout(request)
    HttpResponseRedirect('/?message=success')


def register_action(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        email = request.POST.get('email', None)
        if username and password and repassword and email:
            if password is not repassword:
                return HttpResponseRedirect('/SingUp/?message=error')
            user = User.objects.create_user(username=username,
                                            email=password,
                                            password=email)
        user.is_active = False
        user.save()
        return HttpResponseRedirect
