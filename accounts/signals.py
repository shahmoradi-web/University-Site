from django.db.models.signals import pre_save
from django.dispatch import receiver
from users.models import StudentProfile,TeacherProfile
from random import random

@receiver(pre_save, sender=StudentProfile)
def set_student_id(sender,instance,**kwargs):
    number = f'{int(str(random())[2:5])}{instance.entry_term}'
    instance.student_id = int(number)


@receiver(pre_save, sender=TeacherProfile)
def set_teacher_code(sender,instance,**kwargs):
    number = f'{int(str(random())[2:5])}'
    instance.teacher_code = int(number)
