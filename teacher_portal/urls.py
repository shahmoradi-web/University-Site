from django.urls import path
from.views import *

app_name='teacher_portal'
urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('edit/teacher_profile/', edit_teacher_profile, name='edit_teacher_profile'),
]