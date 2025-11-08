from django.urls import path

from .views import *

app_name='student_portal'
urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('edit/student_profile/', edit_student_profile, name='edit_student_profile'),
    path('add_courses/',student_add_courses,name='student_add_courses'),
    path('show_student_courses/',show_student_courses,name='show_student_courses'),
]