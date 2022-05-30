""" System module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestRegister(TestCase):
    """ Test Register Function """
    def test_register_user(self):
        response = self.client.post(reverse('register'), data={
            'username': 'Aiokdn',
            'email': 'aiokdjb@gmail.com',
            'password1': '123456',
            'password2': '123456'
        })
        self.assertEqual(response.status_code, 302)

        def test_register_user_not_valid(self):
            response = self.client.post(reverse('register'), data={
                'username': 'Aiokdn',
                'email': 'aiokdjb@gmail.com',
                'password1': '123456',
                'password2': '123456'
            })
        
        def test_register_user_get(self):
            response = self.client.get(reverse('register'))
            self.assertEqual(response.status_code, 200)