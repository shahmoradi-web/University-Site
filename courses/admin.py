from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'teacher','credit'
    ]
    list_filter = ['teacher', 'credit']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course','user','teacher']
    list_filter = ['course','user','teacher', 'enrolled_at','status']
    search_fields = ['enrolled_at','status', 'enrolled_at']
    ordering = ['enrolled_at']