import json

from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from log.models import UserProfile
from log.tasks import log_create


@receiver(post_save, sender=LogEntry)
def log_entry_created_updated(sender, instance, created, **kwargs):
    if instance.action_flag == DELETION:
        log_text = f"(ID: {instance.object_id} - {instance.content_type} - {instance.object_repr}) has been deleted"
    if created:
        if instance.action_flag == ADDITION:
            log_text = f"(ID: {instance.object_id} - {instance.content_type} - {instance.object_repr}) has been created"
        elif instance.action_flag == CHANGE:
            change_message = instance.change_message
            change_data = json.loads(change_message)
            formatted_changes = []

            for change in change_data:
                if 'changed' in change:
                    field_changes = change['changed']['fields']
                    formatted_changes.append(', '.join(field_changes))

            human_readable_change_message = '; '.join(formatted_changes)
            log_text = f"updated an object (ID: {instance.object_id}) in the {instance.content_type} model. Changed fields: {human_readable_change_message}"
    else:
        if instance.action_flag == CHANGE:
            change_message = instance.change_message
            change_data = json.loads(change_message)
            formatted_changes = []

            for change in change_data:
                if 'changed' in change:
                    field_changes = change['changed']['fields']
                    formatted_changes.append(', '.join(field_changes))

            human_readable_change_message = '; '.join(formatted_changes)
            log_text = f"updated an object (ID: {instance.object_id}) in the {instance.content_type} model. Changed fields: {human_readable_change_message}"
    get_user = UserProfile.objects.get(user_id=instance.user_id)
    log_create.delay(
        unique_id=int(get_user.unique_id), user_id=int(get_user.user_id), log_content=str(log_text), blockchain="eth"
    )
