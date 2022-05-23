from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import numpy as np
from django.conf import settings 

# Create your models here.


class BreedGroup(models.Model):
    """ Create a breed group model form """
    breed_group = models.CharField(max_length=200)

    def __str__(self):
        """ Return breed group name string """
        return str(self.breed_group).lower()

    def get_absolute_url(self):
        """ Redirect user to add review page"""
        return reverse('add_review')


class Breed(models.Model):
    """ Create a breed model form"""
    breed_name = models.CharField(max_length=200, unique=True)
    group = models.ManyToManyField(BreedGroup)

    def __str__(self):
        """ Return breed name string """
        return str(self.breed_name).lower()

    def get_absolute_url(self):
        """ Redirect user to add review """
        return reverse('add_review')


class BreedReview(models.Model):
    """ Create a breed review model form"""
    ADAPTABILITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    FRIENDLINESS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    TRAINABILITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    HEALTH_GROOMING_NEEDS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    breed_group = models.ForeignKey(BreedGroup, on_delete=models.CASCADE, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=True)
    breed_image = CloudinaryField('image', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=200)
    adaptability = models.IntegerField(choices=ADAPTABILITY_CHOICES)
    friendliness = models.IntegerField(choices=FRIENDLINESS_CHOICES)
    trainability = models.IntegerField(choices=TRAINABILITY_CHOICES)
    health_and_grooming_needs = models.IntegerField(choices=HEALTH_GROOMING_NEEDS_CHOICES)
    # rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return str(self.breed) + '|' + str(self.user_name)

    def get_absolute_url(self):
        return reverse('review_list', kwargs={'pk': self.pk})


breed_review = BreedReview.objects.all()
