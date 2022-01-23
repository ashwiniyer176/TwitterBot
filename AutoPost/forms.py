from django.forms import ModelForm, widgets
from . import models


class MessageForm(ModelForm):
    class Meta:
        model = models.Message
        fields = ['message', 'date_published', 'time_published']
        widgets = {
            'date_published': widgets.DateInput(attrs={'type': 'date'}),
            'time_published': widgets.DateInput(attrs={'type': 'time'})
        }
