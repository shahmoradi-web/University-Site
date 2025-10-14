from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'student_id',
        'department',
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
        'department',
        'grade',
    ]
    ordering = ('student_id',)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'department',
        'teacher_code'
    ]
    search_fields = [
        'user__username',
        'department',
        'teacher_code'
    ]
    list_filter = [
        'department',
        'teacher_code',
    ]
    ordering = ('teacher_code',)