import hashlib

from django.contrib import admin, messages
from django.utils.html import format_html

from .models import LogEntry, UserProfile


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'data', 'get_link', 'blockchain', 'created_at', 'updated_at')
    search_fields = ('user_profile',)
    exclude = ('data_hash',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    @staticmethod
    def get_link(obj):
        if obj.data_hash == "Pending...":
            html_text = '<b style="background-color: #151515 ; color: orange; padding: 6px 10px; text-align: center; border-radius: 5px;">Pending...</b>'
            return format_html(html_text, obj.data_hash)
        else:
            html_text = '<b style="background-color: #151515 ; color: green; padding: 6px 10px; text-align: center; border-radius: 5px;">\
                        <a href="https://sepolia.etherscan.io/tx/{}">Link Created</a></b>'
            return format_html(html_text, obj.data_hash)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'unique_id')
    search_fields = ('user__username',)
    readonly_fields = ('unique_id',)
