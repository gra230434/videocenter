from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        if request.user.get_full_name() is not None:
            context = {'username': request.user.get_full_name()}
        else:
            context = {'username': request.user.get_username()}
        return render(request, 'vcenter/index.html', context)
    else:
        return HttpResponseRedirect('/SingIn/')
