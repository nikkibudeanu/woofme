"""System module"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import SignUpForm


class SignupFormTest(TestCase):
    """ test signup form"""
    def test_if_form_is_valid(self):
        """ is signup form valid?"""
        form = SignUpForm(data={
            "username": "andrea",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea@gmail.com"
        })
        self.assertTrue(form.is_valid())

    def test_if_form_is_invalid(self):
        """ signup form is not valid"""
        form = SignUpForm(data={
            "username": "andrea",
            "password1": "123456",
            "password2": "4367575",
            "email": "andrea@gmail.com"
        })
        self.assertFalse(form.is_valid())
