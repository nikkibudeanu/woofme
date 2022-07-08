""" System module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class TestRegister(TestCase):
    """ Test Register Function """
    def test_register_user(self):
        """ Test redirection after user registration"""
        response = self.client.post(reverse('register'), data={
            'username': 'Aiokdn',
            'email': 'aiokdjb@gmail.com',
            'password1': '123456',
            'password2': '123456'
        })
        self.assertEqual(response.status_code, 302)

    def test_register_user_not_valid(self):
            """ Test view if user is not valid """
            response = self.client.post(reverse('register'), data={
                'username': 'Aiokdn',
                'email': 'aiokdjb@gmail.com',
                'password1': '12345a',
                'password2': '123456'
            })
            self.assertEqual(response.status_code, 302)
     
    def test_register_user_get(self):
            """ Test redirect if user is invalid is correct"""
            response = self.client.get(reverse('register'))
            self.assertEqual(response.status_code, 200)
    
class TestLogin(TestCase):
    """ Test login function"""
    def setUp(self):
        """ Setup user to test login"""
        self.user = User.objects.create_user(
            username='Aiokdn',
            email='aiokdn@gmail.com',
            password='12345')

    def test_if_user_can_login(self):
        """ Test redirection if user logs in"""
        response = self.client.post(reverse(
            'login'),{
            "username": "nikki",
            "password":"12345"})
        self.assertRedirects(
            response, '/users/login_user',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_if_user_cannot_login(self):
        """ Test redirection is user is not able to login"""
        response = self.client.post(reverse(
            'login'),{
                "username": "",
                "password": "12345"
                })
        self.assertRedirects(
                response, '/users/login_user',
                status_code=302,
                target_status_code=200,
                fetch_redirect_response=True)


class TestLogout(TestCase):
    """ Test logout function"""
    def setUp(self):
        """ Setup user to test logout"""
        self.user = User.objects.create_user(
            username='nikki',
            email='nikki@gmail.com',
            password='12345'
            )
    
    def test_logout(self):
        """ Test redirection if user is logged out"""
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/', status_code=302)