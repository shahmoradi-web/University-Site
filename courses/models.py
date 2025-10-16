
from UniversitySite.settings import AUTH_USER_MODEL as User
from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    credit = models.IntegerField(default=3)

    def __str__(self):
        return self.name


