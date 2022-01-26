from django.db import models

# Create your models here.


class Message(models.Model):
    message = models.TextField("Message")
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_published = models.DateField()
    time_published = models.TimeField()
    sent = models.BooleanField(default=False)
    
