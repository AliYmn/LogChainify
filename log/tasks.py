import hashlib
import logging

from celery import shared_task

from log.service import EthereumService

logger = logging.getLogger(__name__)


@shared_task
def log_create(unique_id, user_id, log_content, blockchain):
    from log.models import LogEntry, UserProfile

    eth_service = EthereumService(unique_id, log_content)
    send_log_data = eth_service.send_log_data(unique_id, log_content)
    get_user = UserProfile.objects.get(unique_id=unique_id, user_id=user_id)
    LogEntry.objects.create(user_profile=get_user, data=log_content, data_hash=send_log_data["hash"])
    return "SUCCESS"
