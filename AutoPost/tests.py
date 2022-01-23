from django.test import TestCase
from django.urls import reverse
from . import forms
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
