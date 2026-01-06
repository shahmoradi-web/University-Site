
# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'user_type', 'department', 'is_active')
    list_filter = ('user_type', 'department', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات تکمیلی', {'fields': ('user_type', 'department')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('تاریخ‌ها', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'user_type', 'department', 'password1', 'password2'),
        }),
    )

    search_fields = ('username',)
    ordering = ('username',)
