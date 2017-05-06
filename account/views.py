from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.user.is_authenticated():
        fromuser = request.user
        context = {'username': fromuser.get_username()}
        firstname = request.user.get_short_name()
        fullname = request.user.get_full_name()
        context['firstname'] = firstname
        if firstname is '':
            context['lastname'] = fullname
        else:
            context['lastname'] = fullname.repalce(firstname, "")
        return render(request, 'account/index.html', context)
    else:
        return HttpResponseRedirect('/SingIn/')


def edit(request):
    if request.user.is_authenticated():
        context = {}
        if request.POST:
            is_change = False
            if request.POST['first_name']:
                request.user.first_name = request.POST['first_name']
            if request.POST['last_name']:
                request.user.last_name = request.POST['last_name']
            if is_change:
                request.user.save()
                return HttpResponseRedirect('/acount/')
            context['message'] = "You didn't change anything."
            return render(request, 'account/edit.html', context)
        else:
            firstname = request.user.get_short_name()
            fullname = request.user.get_full_name()
            context['firstname'] = firstname
            context['lastname'] = fullname.repalce(firstname, "")
            return render(request, 'account/edit.html', context)
    else:
        HttpResponseRedirect('/SingIn/')
