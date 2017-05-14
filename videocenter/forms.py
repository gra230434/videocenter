import os

from django import forms
from django.conf import settings
from django.forms import ModelForm

from .models import Animate


class CreateAnimateForm(ModelForm):
    animate = forms.CharField(max_length=256, required=True,)
    animateEN = forms.CharField(max_length=256, required=True,)

    class Meta:
        model = Animate
        fields = ['animate', 'animateEN']

    def save(self):
        name = self.cleaned_data["animate"]
        nameEN = self.cleaned_data["animateEN"]
        folderpath = os.path.join(settings.MEDIA_ROOT, nameEN)
        if os.path.isdir(folderpath):
            if not os.mkdir(folderpath, '0755'):
                msg = {'error': "Can't create a new folder."}
        else:
            msg = {'error': "EN name is exit, please change."}
        if


class AnimateEditForm(ModelForm):
    """docstring for ."""
    year = forms.ChoiceField(label="which year", required=True,)
    season = forms.ChoiceField(label="which season", required=True,)
    is_end = forms.BooleanField(label="the end", required=True,)
    Image = forms.ImageField(label="animate picture", required=False,)
