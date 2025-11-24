from django.db import models
from accounts.models import CustomUser
from courses.models import Course


# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True, null=True, blank=True)
    father_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    entry_term = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} => {self.student_id}'


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher_code = models.IntegerField(unique=True,null=True, blank=True)
    courses = models.ManyToManyField(Course,null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} => {self.teacher_code}'

