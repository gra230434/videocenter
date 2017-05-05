from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        context = {'username': 'username'}
        if request.user.get_full_name() is not None:
            context['username'] = request.user.get_full_name()
        else:
            context['username'] = request.user.get_username()
        context['account'] = request.user.get_username()
        context['text'] = "Try and Error"
        return render(request, 'vcenter/index.html', context)
    else:
        return HttpResponseRedirect('/SingIn/')
