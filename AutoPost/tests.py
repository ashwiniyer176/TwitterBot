from datetime import datetime, timedelta, time
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
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()),
            "time_published": str(time(now.hour, now.minute))
        })
        self.assertTrue(form.is_valid())

    def test_form_with_yesterday(self):
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()-timedelta(days=1)),
            "time_published": "12:34"
        })
        self.assertTrue(form.hasDatePassed(
            datetime.now().date()-timedelta(days=1)))
        self.assertFalse(form.is_valid())

    def test_form_with_today(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()),
            "time_published": str(time(now.hour, min(59, now.minute+2)))
        })
        self.assertFalse(form.hasDatePassed(datetime.now().date()))
        self.assertFalse(form.hasTimePassed(
            time(now.hour, min(59, now.minute+2))))
        self.assertTrue(form.is_valid())

    def test_form_with_tomorrow(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()+timedelta(days=1)),
            "time_published": str(time(now.hour, max(0, now.minute-2)))
        })
        self.assertFalse(form.hasDatePassed(
            datetime.now().date()+timedelta(days=1)))
        self.assertTrue(form.hasTimePassed(
            time(max(0, now.hour-1), now.minute)))
        self.assertTrue(form.is_valid())

    def test_form_with_earlier_time(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()),
            "time_published": str(time(now.hour-1, now.minute-1))
        })
        self.assertTrue(form.hasTimePassed(time(now.hour-1, now.minute-1)))
        self.assertFalse(form.is_valid())

    def test_form_with_future_time(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()),
            "time_published": str(time(now.hour+1, now.minute))
        })
        self.assertFalse(form.hasTimePassed(time(now.hour+1, now.minute)))
        self.assertTrue(form.is_valid())

    def test_form_with_current_time(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "date_published": str(datetime.now().date()),
            "time_published": str(time(now.hour, now.minute))
        })
        self.assertFalse(form.hasTimePassed(time(now.hour, now.minute)))
        self.assertTrue(form.is_valid())
