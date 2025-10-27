from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns =[
    path('', home, name='home'),
    path('register/students/', register_students, name='register_students'),
    path('register/teachers/', register_teachers, name='register_teachers'),
    path('register/admin/', register_admin, name='register_admin'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
]