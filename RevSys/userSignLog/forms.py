from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Full Name',
            'id': 'fullName',
            'required': True,
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'Email Address',
            'id': 'email',
            'required': True,
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Password',
            'id': 'password',
            'required': True,
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Confirm Password',
            'id': 'confirmPassword',
            'required': True,
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'login-input',
            'placeholder': 'Email',
            'id': 'email',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login-input',
            'placeholder': 'Password',
            'id': 'password',
            'required': True,
        })
    )
