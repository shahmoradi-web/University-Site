from django.urls import path
from . import views

app_name='api'
urlpatterns =[
    path('courses/',views.CoursesListAPIView.as_view(),name='course-list'),
    path('courses/<int:pk>',views.CourseDetailAPIView.as_view(),name='course-detail'),
]