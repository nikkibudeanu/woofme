""" System module"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedReview, Breed, BreedGroup


class SetupViewTestCase(TestCase):
    """ Test case for all view tests"""
    def setUp(self):
        self.breed = Breed.objects.create(name='Breed')
        self.breed_group = BreedGroup.objects.create(breed_group= 'group')
        self.breed_review = BreedReview.objects.create(
            breed_group=self.breed_group,
            breed=self.breed,
            user_name=user,
            published_date='Oct. 25, 2021, 9:45 p.m.',
            review='Review test',
            adaptability='5',
            trainability='5',
            friendliness='5',
            health_and_grooming_needs='5',
            rating='5')
        self.url = reverse('edit_review', kwargs={
            'pk': self.breed_review.id
        })

class BreedRatingView(SetupViewTestCase):
    """ Test Breed Rating view response, if correct url and template"""
    def test_breed_rating_view_success_status_code(self):
        """ Test review list page url """
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_view_by_name(self):
        """ Test review list page by name"""
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_view_if_correct_template(self):
        """ Test if review list is rendering correct template """
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_breed_rating_view_incorrect_html(self):
        """ Test if the review list is rendering the wrong html and display message if it is"""
        response = self.client.get(reverse('review_list'))
        self.assertNotContains(response, 'Hello friend! I am on the wrong page!')

    def test_breed_rating_view_valid_html(self):
        """ Test if the review list is showing the correct html"""
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, 'Latest Reviews of your favorite breeds!')


