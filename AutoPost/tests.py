from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import reverse
from . import forms
from . import views
# Create your tests here.


class FormTest(TestCase):
    def test_page_is_reachable(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_form_without_message(self):
        form = forms.MessageForm(data={
            "message": " ",
            "date_published": "2020-12-1",
            "time_published": "12:34"
        })
        self.assertFalse(form.is_valid())

    def test_form_without_date(self):
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": "",
            "time_published": "12:34"
        })
        self.assertFalse(form.is_valid())

    def test_form_without_time(self):
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": "2020-12-21",
            "time_published": ""
        })
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": "2020-10-4",
            "time_published": "12:34"
        })
        self.assertTrue(form.is_valid())

    def test_hasDatePassed_yesterday(self):
        yesterday = str(datetime.now().date()-timedelta(days=1))
        self.assertTrue(views.hasDatePassed(yesterday))

    def test_hasDatePassed_today(self):
        today = str(datetime.now().date())
        self.assertFalse(views.hasDatePassed(today))

    def test_hasDatePassed_tomorrow(self):
        tomorrow = str(datetime.now().date()+timedelta(days=1))
        self.assertFalse(views.hasDatePassed(tomorrow))

    def test_hasTimePassed_now(self):
        currentTime = str(datetime.now().time().hour) + \
            ":" + str(datetime.now().minute)
        self.assertFalse(views.hasTimePassed(currentTime))

    def test_hasTimePassed_past(self):
        past = str(datetime.now().time().hour-1) + \
            ":" + str(datetime.now().minute)
        self.assertTrue(views.hasTimePassed(past))

    def test_hasTimePassed_future(self):
        future = str(datetime.now().time().hour+1) + \
            ":" + str(datetime.now().minute)
        self.assertFalse(views.hasTimePassed(future))
