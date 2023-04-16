import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(name="log_message")
def log_message(message):
    logger.info(f"Log message from task: {message}")
    return f"Logged message: {message}"
