from django.urls import path
from.views import *

app_name='teacher_portal'
urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('edit/teacher_profile/', edit_teacher_profile, name='edit_teacher_profile'),
    path('add_courses/', teacher_add_courses, name='teacher_add_courses'),
    path('show_courses/', show_courses, name='show_courses'),
]