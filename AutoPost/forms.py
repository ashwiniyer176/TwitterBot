from django.forms import ModelForm, widgets, ValidationError
from . import models
import datetime


class MessageForm(ModelForm):
    class Meta:
        model = models.Message
        fields = ['message', 'date_published', 'time_published']
        widgets = {
            'date_published': widgets.DateInput(attrs={'type': 'date'}),
            'time_published': widgets.DateInput(attrs={'type': 'time'})
        }

    def hasDatePassed(self, date):
        '''
        date(datetime.date): format YYYY-MM-DD
        '''
        if(datetime.datetime.now().date() > date):
            return True
        return False

    def hasTimePassed(self, time):
        '''
        time(datetime.time): format HH:MM (24 hr format)
        '''
        if(datetime.datetime.now().time().hour < time.hour):
            return False
        elif(datetime.datetime.now().time().hour == time.hour):
            if(datetime.datetime.now().time().minute <= time.minute):
                return False
            else:
                return True
        else:
            return True

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        if len(cleaned_data.keys()) != 3:
            raise ValidationError("Incomplete Form")
        else:
            if self.hasDatePassed(cleaned_data['date_published']):
                raise ValidationError("Date has already passed")
            elif self.hasTimePassed(cleaned_data['time_published']) and cleaned_data['date_published'] == datetime.datetime.now().date():
                raise ValidationError("TIme has passed")
            else:
                return cleaned_data
