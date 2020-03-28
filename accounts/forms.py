from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class LoginModelForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus':'autofocus'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']

