""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from woofme_app.models import BreedReview, Breed, BreedGroup


class TestErrors(TestCase):
    """ Test raised 404 error page """
    def test_not_found_view(self):
        """ Test if review page url exist """
        response = self.client.get(
            '/review_list/review_page/0')
        self.assertEqual(response.status_code, 404)
