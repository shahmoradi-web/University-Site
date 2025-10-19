from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns =[
    path('', home, name='home'),
    path('register/users/', register_users, name='register_users'),
]