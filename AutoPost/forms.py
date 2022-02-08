from django.forms import ModelForm, widgets, ValidationError
from . import models
import datetime


class MessageForm(ModelForm):
    class Meta:
        model = models.Message
        fields = ['message', 'author']
