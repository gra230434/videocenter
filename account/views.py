from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .function.accountget import getlastname


# Create your views here.
@login_required
def index(request):
    context = {}
    if request.GET:
        msg = request.GET['msg']
        if msg is 200:
            context['message'] = "success"
        elif msg is 201:
            context['message'] = "You didn't iuput first name."
    context['username'] = request.user.get_username()
    context['firstname'] = request.user.get_short_name()
    context['lastname'] = getlastname(request.user)
    return render(request, 'account/index.html', context)


@login_required
def edit(request):
    context = {}
    context['username'] = request.user.get_username()
    userlastname = getlastname(request.user)
    if request.POST:
        firstname = request.POST.get(['first_name'], None)
        lasttname = request.POST.get(['last_name'], None)
        if firstname is not None:
            request.user.first_name = firstname
            if lasttname is not None and lasttname is not userlastname:
                request.user.last_name = lasttname
            request.user.save()
            return HttpResponseRedirect('/account/?msg=200')
        if firstname is None and lasttname is not None:
            request.user.first_name = lasttname
            request.user.last_name = ''
            request.user.save()
            return HttpResponseRedirect('/account/?msg=201')
        context['message'] = "You didn't change anything."
        return render(request, 'account/edit.html', context)
    else:
        context['firstname'] = request.user.get_short_name()
        context['lastname'] = getlastname(request.user)
        return render(request, 'account/edit.html', context)
