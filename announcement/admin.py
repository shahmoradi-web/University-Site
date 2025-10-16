from django.contrib import admin

from announcement.models import Announcement


# Register your models here.


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'content','course', 'audience']
    list_filter = ['title', 'content', 'course', 'audience']
    search_fields = ['title', 'audience']
    ordering = ['title']
