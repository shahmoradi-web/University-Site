from django.db import models

from accounts.models import CustomUser
from courses.models import Course


# Create your models here.

class Announcement(models.Model):
    AUDIENCE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('all', 'All')
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    audience = models.CharField(max_length=100, choices=AUDIENCE_CHOICES, default='all')

