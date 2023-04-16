from django.db.models.signals import post_save
from django.dispatch import receiver

from log.models import LogEntry
from log.tasks import log_create


@receiver(post_save, sender=LogEntry)
def log_post_save(sender, instance, created, **kwargs):
    if instance.data_hash == "Pending...":
        log_create.delay(
            blockchain=instance.blockchain,
            log_id=instance.id,
            unique_id=int(instance.user_profile.unique_id),
            user_id=int(instance.user_profile.user_id),
            log_content=str(instance.data),
        )
