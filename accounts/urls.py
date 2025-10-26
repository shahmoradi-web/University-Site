from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns =[
    path('', home, name='home'),
    path('register/students/', register_students, name='register_students'),
    path('register/teachers/', register_teachers, name='register_teachers'),
]