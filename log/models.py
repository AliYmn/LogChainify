import hashlib
import random

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.IntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        unique_id = random.randint(100000, 999999)
        while UserProfile.objects.filter(unique_id=unique_id).exists():
            unique_id = random.randint(100000, 999999)
        return unique_id


class LogEntry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    data = models.TextField()
    BLOCKCHAIN_CHOICES = [
        ('eth', 'Ethereum'),
        ('btc', 'Bitcoin'),
        ('doge', 'Dogecoin'),
        ('ltc', 'Litecoin'),
    ]
    blockchain = models.CharField(max_length=4, choices=BLOCKCHAIN_CHOICES, default='eth')
    data_hash = models.CharField(max_length=100, default="Pending...")
    secure_hash = models.CharField(max_length=100, default="Pending...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_profile.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
