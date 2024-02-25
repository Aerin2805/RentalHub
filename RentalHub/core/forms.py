from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )

class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email address', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': INPUT_CLASSES, 'style': 'color: white; background-color: #1a202c;'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
