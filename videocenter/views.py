from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    context = {'username': 'username'}
    if request.user.get_short_name() is not None:
        context['username'] = request.user.get_short_name()
    else:
        context['username'] = request.user.get_username()
    context['account'] = request.user.get_username()
    context['text'] = "Try and Error"
    return render(request, 'vcenter/index.html', context)

