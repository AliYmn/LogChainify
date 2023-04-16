from django.contrib import admin

from .models import LogEntry, UserProfile


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'data',
        'data_hash',
        'timestamp',
    )
    search_fields = ('user_profile',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
