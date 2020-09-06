from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)