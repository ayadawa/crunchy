from django.contrib.auth.models import User
from django import forms
from hotels.models import Hotel



class UserForm(forms.ModelForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'User Name','class' : 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

