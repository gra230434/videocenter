from django import forms
from django.forms import ModelForm

from .models import Animate
from .models import AnimateDetail


class CreateAnimateForm(ModelForm):
    animate = forms.CharField(max_length=256, required=True,)
    animateEN = forms.CharField(max_length=256, required=True,)

    class Meta:
        model = Animate
        fields = ['animate', 'animateEN']


class EditAnimateForm(ModelForm):
    """docstring for ."""
    year = forms.ChoiceField(label="which year", required=True,)
    season = forms.ChoiceField(label="which season", required=True,)
    is_end = forms.BooleanField(label="the end", required=True,)
    Image = forms.ImageField(label="animate picture", required=False,)

    class Meta:
        model = AnimateDetail
        fields = ['year', 'season', 'is_end']
