from django.shortcuts import render

import courses
from api.serializer import CourseSerializer, StudentSerializer, TeacherSerializer
from courses.models import Course, Enrollment
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import StudentProfile, TeacherProfile


# Create your views here.


class CoursesListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
    # def get_queryset(self):
    #     teacher = TeacherProfile.objects.get(user=self.request.user)
    #     teacher_courses = teacher.courses.all()
    #     students_enrollment = Enrollment.objects.filter(courses__in=teacher_courses).distinct()
    #     return students


class StudentDetailAPIView(generics.RetrieveAPIView):

    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer

class TeacherListAPIView(generics.ListAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailAPIView(generics.RetrieveAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer