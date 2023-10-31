from django import forms
from django.forms import ModelForm
from .models import Profile

# profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','wallet_address','private_key',)
