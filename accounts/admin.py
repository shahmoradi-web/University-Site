from django.contrib import admin
from accounts.models import *

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'user_type',
        'department'
    ]
    list_filter = ['user_type', 'department']
    search_fields = ['username', 'user_type', 'department']
    ordering = ['username']