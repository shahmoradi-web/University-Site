from django.shortcuts import render

import courses
from api.serializer import CourseSerializer
from courses.models import Course
from rest_framework import generics


# Create your views here.


class CoursesListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
