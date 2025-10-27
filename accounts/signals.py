from django.db.models.signals import pre_save
from django.dispatch import receiver
from users.models import StudentProfile,TeacherProfile
from random import random

@receiver(pre_save, sender=StudentProfile)
def set_student_id(sender,instance,**kwargs):
    instance.student_id = f'{int(str(random)[2:])}{instance.entry_term}'


@receiver(pre_save, sender=TeacherProfile)
def set_teacher_code(sender,instance,**kwargs):
    instance.teacher_code = f'{int(str(random)[2:])}'
