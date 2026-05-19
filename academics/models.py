from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="majors")

    def __str__(self):
        return self.name
