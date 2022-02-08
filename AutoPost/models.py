
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    message = models.TextField("Message")
    author = models.CharField("Author", default="Anonymous", max_length=50)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.message + " - " + self.author

    def toggle_message_status(self):
        self.sent = True
        self.save()
