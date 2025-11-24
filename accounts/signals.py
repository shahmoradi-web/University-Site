from django.db.models.signals import pre_save
from django.dispatch import receiver
from users.models import StudentProfile,TeacherProfile
from random import random,randint

@receiver(pre_save, sender=StudentProfile)
def set_student_id(sender,instance,**kwargs):
    if not instance.student_id:
        rand = randint(100, 999)  # فقط عدد
        number = f"{rand}{instance.entry_term}"
        instance.student_id = int(number)


@receiver(pre_save, sender=TeacherProfile)
def set_teacher_code(sender,instance,**kwargs):
    if not instance.teacher_code:
        rand = randint(100, 999)  # فقط عدد
        instance.teacher_code = rand