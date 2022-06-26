"""System module"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import SignupForm


class SignupFormTest(TestCase):
    """ test signup form"""
    def test_if_form_is_valid(self):
        """ is signup form valid?"""
        form = SignupForm(data={
            "username": "andrea",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea@gmail.com"
        })
        self.assertTrue(form.is_valid())

    def test_if_form_password_is_invalid(self):
        """ signup form passsword is not valid"""
        form = SignupForm(data={
            "username": "andrea",
            "password1": "12345",
            "password2": "54321",
            "email": "andrea@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_form_email_invalid(self):
        """ signup form has invalid email"""
        form = SignupForm(data={
            "username": "andrea",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea;gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_form_empty_username(self):
        """ form has empty username"""
        form = SignupForm(data={
            "username": "",
            "password1": "123456",
            "password2": "123456",
            "email": "andrea@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_form_lower_username(self):
        """ test if form's username is lower"""
        form = SignupForm(data={
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
        form = SignupForm(data={
            "username": "andrea"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(str(self.user.username), "andrea")
        self.assertRaises(ValidationError)

    def test_form_email_duplicated(self):
        """ test if email is duplicated """
        form = SignupForm(data={
            "email": "andrea@gmail.com"
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    def test_form_incorrect_password2(self):
        """ test if passwords do not match"""
        form = SignupForm(data={
            "password1": "12345678",
            "password2": "1234"
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    
