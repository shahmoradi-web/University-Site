from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *
from django import forms
from users.models import StudentProfile
from accounts.models import CustomUser


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'department', 'password1', 'password2']


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

class EditTeacherProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']
