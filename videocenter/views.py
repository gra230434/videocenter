import os

from django.conf import settings
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import AnimateDetail
from .forms import CreateAnimateForm
from .forms import EditAnimateForm


# Create your views here.
@login_required
def index(request):
    context = {'username': 'username'}
    if request.user.get_short_name() is not None:
        context['username'] = request.user.get_short_name()
    else:
        context['username'] = request.user.get_username()
    return render(request, 'vcenter/index.html', context)


@login_required
def animate(request):
    context = {'animate': []}
    if request.user.get_short_name() is not None:
        context['username'] = request.user.get_short_name()
    else:
        context['username'] = request.user.get_username()
    try:
        AniList = AnimateDetail.objects.order_by('update')[0:1].get()
        for val in AniList:
            context['animate'].append(val.animateDict())
        return render(request, 'vcenter/animate.html', context)
    except:
        context['error'] = "Please contact me."
    return render(request, 'vcenter/animate.html', context)


@login_required
def anidetail(request, aniID):
    if aniID is not None:
        try:
            andetail = AnimateDetail.objects.get(ID=aniID)
            context = {
                'aniname': andetail.animate,
                'aninameEN': andetail.animateEN,
                'year': andetail.year,
                'season': andetail.season,
                'is_end': andetail.is_end,
                }
            return render(request, 'vcenter/anidetail.html', context)
        except AnimateDetail.DoesNotExist:
            return HttpResponseRedirect('vcenter/animate/')
    else:
        return HttpResponseRedirect('vcenter/animate/')


@login_required
def editanicreate(request):
    if request.method == 'POST':
        form = CreateAnimateForm(request.POST)
        if form.is_valid():
            name = request.POST['animate']
            nameEN = request.POST['animateEN']
            season = 1
            nameENSE = "{}_SO{}".format(nameEN, str(season).zfill(2))
            while os.path.isdir(os.path.join(settings.MEDIA_ROOT,
                                             'ani', nameENSE)):
                season += 1
                nameENSE = "{}_SO{}".format(nameEN, str(season).zfill(2))
            if not os.mkdirs(os.path.join(settings.MEDIA_ROOT, nameENSE),
                             '0755'):
                context = {'error': 'create folder fail',
                           'form': CreateAnimateForm()}
                return render(request, 'vcenter/editani.html', context)
            form.save()
            AD = AnimateDetail(animate=name, animateEN=nameEN,
                               sequence=str(season).zfill(2))
            AD.save()
            return redirect('vcenter_anidetail', AD.id)
    else:
        form = CreateAnimateForm()
        return render(request, 'vcenter/editani.html', {'form': form})


class editanidetail(LoginRequiredMixin, View):
    """docstring for editanidetail."""
    def get(self, request, aniID, is_fail=None):
        if aniID is not None:
            try:
                andetail = AnimateDetail.objects.get(ID=aniID)
                aniname = andetail.animate
                aninameEN = andetail.animateEN
                form = EditAnimateForm()
                context = {'name': aniname,
                           'nameEN': aninameEN,
                           'form': form}
                if is_fail is not None:
                    context['erroe'] = "Update fail"
                return render(request, 'vcenter/editanidetail.html', context)
            except AnimateDetail.DoesNotExist:
                return HttpResponseRedirect('vcenter/animate/')
        else:
            return HttpResponseRedirect('vcenter/animate/')

    def post(self, request, aniID):
        if aniID is not None:
            try:
                AnimateDetail.objects.get(ID=aniID)
            except AnimateDetail.DoesNotExist:
                return HttpResponseRedirect('vcenter/animate/')
            instance = get_object_or_404(AnimateDetail, id=aniID)
            form = EditAnimateForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('vcenter_anidetail', aniID)
            return redirect('VC_edit_anidetail', aniID, 'fail')
        else:
            return HttpResponseRedirect('vcenter/animate/')
