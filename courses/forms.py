from django import forms
from .models import *

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','term','credit']