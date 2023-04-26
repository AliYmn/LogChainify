from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from log.models import UserProfile
from log.tasks import log_create


@receiver(post_save, sender=LogEntry)
def log_entry_created_updated(sender, instance, created, **kwargs):
    if instance.action_flag == DELETION:
        log_text = f"(ID: {instance.object_id} - {instance.content_type}) has been deleted"
    if created:
        if instance.action_flag == ADDITION:
            log_text = f"(ID: {instance.object_id} - {instance.content_type}) has been created"
        elif instance.action_flag == CHANGE:
            log_text = f"(ID: {instance.object_id} - {instance.content_type}) has been updated"
    else:
        if instance.action_flag == CHANGE:
            log_text = f"(ID: {instance.object_id} - {instance.content_type}) has been updated"
    get_user = UserProfile.objects.get(user_id=instance.user_id)
    log_create.delay(
        unique_id=int(get_user.unique_id), user_id=int(get_user.user_id), log_content=str(log_text), blockchain="eth"
    )
