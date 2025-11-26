
from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE ,related_name='teacher_courses')
    term = models.CharField(max_length=100)
    credit = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('passed', 'Passed'),
        ('failed', 'Failed'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_enrollments')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teacher_enrollments')
    grade = models.FloatField(null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='passed')
    def __str__(self):
        return f'{self.user.username} - {self.course} - {self.grade}'