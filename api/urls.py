from django.urls import path
from . import views

app_name='api'
urlpatterns =[
    path('courses/',views.CoursesListAPIView.as_view(),name='course-list'),
    path('courses/<int:pk>',views.CourseDetailAPIView.as_view(),name='course-detail'),
    path('students/',views.StudentListAPIView.as_view(),name='student-list'),
    path('students/<int:pk>',views.StudentDetailAPIView.as_view(),name='student-detail'),
]