""" System module"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedReview, Breed, BreedGroup


class SetupViewTestCase(TestCase):
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


