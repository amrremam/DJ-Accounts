from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile



class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class userform(forms.Modelform):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class profileForm(forms.Modelform):
    class Meta:
        model = profile
        fields = ['phone_number', 'address']