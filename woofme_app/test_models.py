""" System module"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedGroup, Breed, BreedReview


class SetupModelTestCase(TestCase):
    """ Test case for all view tests"""
    def setUp(self):
        """ create user for testing models"""
        self.username = 'anna'
        self.password = '23456'
        user = User.objects.create_user(
            username=self.username,
            email='anna@gmail.com',
            password=self.password
        )
        self.client.login(username='anna', password='23456')
        self.breed = Breed.objects.create(name='Breed')
        self.breed_group = BreedGroup.objects.create(breed_group='Group')
        self.breed_review = BreedReview.objects.create(
            breed_group=self.breed_group,
            breed=self.breed,
            username=user,
            created_at='Nov. 23, 2022, 6:78 p.m.',
            review='Test',
            adaptability='5',
            friendliness='4',
            trainability='4',
            health_and_grooming_needs='5',
            rating='1'
        )


class BreedGroupTestCase(SetupModelTestCase):
    """ Test breed group model"""
    def test_absolute_url(self):
        """ Test if redirection to add review page is correct """
        self.assertEqual(
            self.breed_group.get_absolute_url(), reverse('add_review'))


class BreedTestCase(SetupModelTestCase):
    """ Test breed model"""
    def test_absolute_url(self):
        """ Test if redirection to add review page is correct """
        self.assertEqual(
            self.breed.get_absolute_url(), reverse('add_review'))


class BreedReviewTestCase(SetupModelTestCase):
    """ Test breedreview model"""
    def test_absolute_url(self):
        """ Test if breed review page is redirecting correctly"""
        self.assertEqual(self.breed_review.get_absolute_url(), reverse(
            'review_page', kwargs={'pk': self.breed_review.id}))

