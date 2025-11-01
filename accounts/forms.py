from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *
from django import forms
from users.models import StudentProfile
from accounts.models import CustomUser



class UserRegisterForm(ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','department']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise ValidationError("Passwords don't match")
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if CustomUser.objects.filter(email=cd['email']).exists():
            raise ValidationError("Email already registered")
        return cd['email']


class StudentRegisterForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['father_name','faculty','entry_term','major']


class LoginUserForm(forms.Form):
    username = forms.CharField(label='نام کاربری', max_length=150)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)

class EditStudentProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']