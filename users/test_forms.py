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


    def test_form_email_invalid(self):
        """ signup form has invalid email"""
        form = SignUpForm(data={
            "username": "andrea",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea;gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_form_empty_username(self):
        """ form has empty username"""
        form = SignUpForm(data={
            "username": "",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_form_lower_username(self):
        """ test if form's username is lower"""
        form = SignUpForm(data={
            "username": "ANDREA",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea@gmail.com"
        })
        self.assertTrue(form.is_valid())
        form.save()
        username = User.objects.get(username='andrea')
        self.assertEqual(str(username.username), "andrea")

class SetupRegisterForm(TestCase):
    """ Setup register """
    def setUp(self):
        self.user = User.objects.create(
            username="andrea",
            password="123456",
            email="andrea@gmail.com"
        )

class SignupFormTestInvalid(SetupRegisterForm):
    """ Test if form fields are not valid"""
    def test_form_username_duplicated(self):
        """ test if username is duplicated """ 
        form = SignUpForm(data={
            "username": "andrea",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(str(self.user.username), "andrea")
        self.assertRaises(ValidationError)