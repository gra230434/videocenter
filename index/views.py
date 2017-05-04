from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Hello, world. You're at the video index."
    context = {'mes': message}
    return render(request, 'index/index.html', context)


def register_page(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Welcome register"
    context = {'message': message}
    return render(request, 'index/register.html', context)


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
