from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class StudentManagerUser(BaseUserManager):

    def create_user(self, student_number, password, **extra_fields):
        if not student_number:
            raise ValueError('Student number required')

        user = self.model(student_number=student_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        self.create_user(student_number, password, **extra_fields)




class StudentUser(AbstractBaseUser, PermissionsMixin):
    student_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    beginning_university_years = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = StudentManagerUser()

    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.student_number} => {self.first_name} {self.last_name}'


