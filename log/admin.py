import hashlib

from django.contrib import admin, messages
from django.utils.html import format_html

from .models import LogEntry, UserProfile


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'data', 'get_link', 'blockchain', 'created_at', 'updated_at')
    search_fields = ('user_profile',)
    # readonly_fields = ('data_hash', 'secure_hash')
    exclude = ('data_hash',)

    def save_model(self, request, obj, form, change):
        secure_hash_txt = (
            str(obj.user_profile.unique_id + obj.user_profile.user_id) + str(obj.data) + str(obj.blockchain)
        )
        secure_hash = hashlib.sha256(secure_hash_txt.encode('utf-8')).hexdigest()
        if obj.secure_hash != "Pending..." and secure_hash != obj.secure_hash:
            messages.error(request, "Age must be greater than or equal to 18")
            return
        super().save_model(request, obj, form, change)

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
