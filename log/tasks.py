import hashlib
import logging

from celery import shared_task

from log.service import EthereumService

logger = logging.getLogger(__name__)


@shared_task
def log_create(unique_id, user_id, log_content, log_id, blockchain):
    from log.models import LogEntry, UserProfile

    eth_service = EthereumService(unique_id, log_content)
    log_hash_txt = str(unique_id + user_id) + str(log_content)
    log_data = hashlib.sha256(log_hash_txt.encode('utf-8')).hexdigest()
    send_log_data = eth_service.send_log_data(unique_id, log_data)
    get_user = UserProfile.objects.get(unique_id=unique_id, user_id=user_id)
    secure_hash_txt = str(unique_id + user_id) + str(log_content) + str(blockchain)
    secure_hash = hashlib.sha256(secure_hash_txt.encode('utf-8')).hexdigest()

    LogEntry.objects.filter(id=log_id).update(
        user_profile=get_user, data=log_content, data_hash=send_log_data["hash"], secure_hash=secure_hash
    )

    return "SUCCESS"
