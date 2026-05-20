from django.db import models

from academics.models import Faculty, Major
from accounts.models import CustomUser
from courses.models import Course


# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/student/',null=True, blank=True)
    student_id = models.IntegerField(unique=True, null=True, blank=True)
    father_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='students',null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='students',null=True, blank=True)
    entry_term = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} => {self.student_id}'


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='teachers',null=True, blank=True)
    photo = models.ImageField(upload_to='images/teacher/',null=True, blank=True)
    teacher_code = models.IntegerField(unique=True,null=True, blank=True)
    courses = models.ManyToManyField(Course,null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} => {self.teacher_code}'

