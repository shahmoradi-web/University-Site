from django.shortcuts import render

import courses
from api.serializer import CourseSerializer, StudentSerializer
from courses.models import Course
from rest_framework import generics

from users.models import StudentProfile


# Create your views here.


class CoursesListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer