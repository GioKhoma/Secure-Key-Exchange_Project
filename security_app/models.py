from django.db import models
from django.conf import settings


class Channel(models.Model):
    sender_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='channels_sent'
    )
    recipient_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='channels_received'
    )
    name = models.CharField(max_length=255, unique=True)
    accepted = models.BooleanField(default=False)
    initial_sender_secret = models.TextField()
    initial_recipient_secret = models.TextField()

    def __str__(self):
        return self.name


