from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class StudentProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    father_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    entry_term = models.CharField(max_length=100)
    grade = models.IntegerField()


class TeacherProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_code = models.IntegerField(unique=True)
