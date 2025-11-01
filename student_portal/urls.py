from django.urls import path

from .views import *

app_name='student_portal'
urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('edit/student_profile/', edit_student_profile, name='edit_student_profile'),
]