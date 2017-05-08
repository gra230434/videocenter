from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text=_('Optional.'))
    last_name = forms.CharField(max_length=30, required=False,
                                help_text=_('Optional.'))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.EmailInput,
                             help_text=_('Required.'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
