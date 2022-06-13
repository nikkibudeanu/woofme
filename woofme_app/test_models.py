from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedGroup, Breed, BreedReview

import logging

class SetupModelTestCase(TestCase):
    """ Test case for all view tests"""
    def setUp(self):
        self.username = 'anna'
        self.password = '23456'
        user = User.objects.create_user(
            username=self.username,
            email='anna@gmail.com',
            password=self.password
        )
        self.client.login(username='anna', password='23456')
        self.breed = Breed.objects.create(breed_name='Breed')
        self.breed_group = BreedGroup.objects.create(breed_group='Group')
        self.breed_review = BreedReview.objects.create(
            breed_group=self.breed_group,
            breed=self.breed,
            username=user,
            published_date='Nov. 23, 2022, 6:78 p.m.',
            review='Test',
            adaptability='5',
            friendliness='4',
            trainability='4',
            health_and_grooming_needs='5',
            rating='1'
        )


class BreedGroupTestCase(SetupModelTestCase):
    """ Test breed group model"""
    def test_abdolute_url(self):
        logging.debug(self.breed_group)
        self.assertEqual(self.breed_group.get_absolute_url(), reverse('add_review'))