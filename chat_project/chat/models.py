from django.conf import settings
from django.db import models
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='sender')
    getter = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='getter')
    text = models.TextField()
    is_red = models.BooleanField()
    sended_time = models.DateTimeField(default=timezone.now)

    def send(self):
        self.sended_time = timezone.now()
        self.is_red = False
        self.save()
