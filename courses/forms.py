from django import forms

from .models import *

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','term','credit']

class CourseSelectForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(),
                                             widget=forms.CheckboxSelectMultiple,
                                             required=True,
                                             label='انتخاب درس ها')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].label_from_instance = lambda obj: f"{obj.name}  {obj.teacher.first_name} {obj.teacher.last_name}  {obj.term}  {obj.credit}"