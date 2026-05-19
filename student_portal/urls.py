from django.urls import path

from .views import *

app_name='student_portal'
urlpatterns =[
    path('dashboard/', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
    path('edit/student_profile/', edit_student_profile, name='edit_student_profile'),
    path('show_student_courses/',show_student_courses,name='show_student_courses'),
    path('show_announcement/',show_announcement,name='show_announcement'),
    path('show_all_courses/',show_all_courses,name='show_all_courses'),
    path('take_courses/',take_courses,name='take_courses'),
    path('save_enrollment/',save_enrollment,name='save_enrollment'),
    path('edit_courses/',edit_courses,name='edit_courses'),
]