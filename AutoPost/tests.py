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
            "author": "Anonymous"
        })
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        now = datetime.now().time()
        form = forms.MessageForm(data={
            "message": "asd ",
            "author": "Xyz"
        })
        self.assertTrue(form.is_valid())
