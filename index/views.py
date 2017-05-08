from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import forms
from .function.notrobot import isrobot


def index(request):
    if 'message' in request.GET:
        message = request.GET['message']
    else:
        message = "Hello, world. You're at the video index."
    context = {'mes': message}
    return render(request, 'index/index.html', context)


def register_page(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            result = isrobot(request.POST.get('g-recaptcha-response'))
            if result['success']:
                form.save()
                return HttpResponseRedirect('/SingIn/')
            else:
                context = {'error': 'Invalid reCAPTCHA. Please try again.',
                           'form': form}
                return render(request, 'index/register.html', context)
        else:
            return render(request, 'index/register.html', {'form': form})
    else:
        form = forms.SignUpForm()
        return render(request, 'index/register.html', {'form': form})
