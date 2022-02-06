
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    message = models.TextField("Message")
    author = models.CharField("Author", default="Anonymous", max_length=50)
    date_published = models.DateField(default=timezone.now().date())
    time_published = models.TimeField(default=timezone.now().time())
    sent = models.BooleanField(default=False)

    def toggle_message_status(self):
        self.sent = True
        self.save()
