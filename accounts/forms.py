from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *
from UniversitySite.settings import AUTH_USER_MODEL as User
from django import forms
from users.models import StudentProfile



class UserRegisterForm(ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password','department']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError("Passwords don't match")
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError("Email already registered")
        return cd['email']


class StudentRegisterForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['father_name','faculty','entry_term','major']
