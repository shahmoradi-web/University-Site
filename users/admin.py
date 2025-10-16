from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [
        'student_id',
        'entry_term'
    ]
    search_fields = [
        'student_id',
        'major',
        'faculty'

    ]
    list_filter = [
        'faculty',
        'entry_term',
        'grade',
    ]
    ordering = ('student_id',)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = [
        'teacher_code'
    ]
    search_fields = [
        'teacher_code'
    ]
    list_filter = [
        'teacher_code',
    ]
    ordering = ('teacher_code',)