import hashlib

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from log.tasks import log_message


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LogEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    data_hash = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.timestamp}'

    def save(self, *args, **kwargs):
        print("###### BURADAAAA ######")
        log_message.delay(f"Saving instance of {self.__class__.__name__} with id {self.pk}")
        calculated_hash = hashlib.sha256(self.data.encode('utf-8')).hexdigest()
        if self.data_hash != calculated_hash:
            pass
            # raise ValidationError('Data hash does not match the calculated hash')

        super().save(*args, **kwargs)
