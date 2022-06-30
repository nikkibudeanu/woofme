""" Imports """
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from slugger import AutoSlugField



class BreedGroup(models.Model):
    """ Create a breed group model form """
    breed_group = models.CharField(max_length=128, unique=True, null=True)
    description = models.TextField(max_length=2000, null=True)
    slug = AutoSlugField(populate_from='breed_group', default='group')


    def __str__(self):
        """ Return breed group name string """
        return str(self.breed_group).lower()

    def get_absolute_url(self):
        """ Redirect user to add review page"""
        return reverse('add_review')


class Breed(models.Model):
    """ Create a breed model form"""
    name = models.CharField(max_length=200, unique=True)
    breed_group = models.ForeignKey(
        BreedGroup, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=50, null=True)
    breed_image = CloudinaryField('image', blank=True, transformation={'width': '600', 'height': '600', 'crop':'fill', 'gravity':"auto"})
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """ Return breed name string """
        return str(self.name).lower()

    def get_absolute_url(self):
        """ Redirect user to add review """
        return reverse('add_review')


class BreedReview(models.Model):
    """ Create a breed review model form"""
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    breed_group = models.ForeignKey(BreedGroup, on_delete=models.CASCADE, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review = models.TextField(max_length=200)
    breed_image = CloudinaryField('image', blank=True, transformation={'width': '600', 'height': '600', 'crop':'fill', 'gravity':"auto"})
    adaptability = models.IntegerField(choices=RATING_CHOICES, default=0)
    friendliness = models.IntegerField(choices=RATING_CHOICES, default=0)
    trainability = models.IntegerField(choices=RATING_CHOICES, default=0)
    health_and_grooming_needs = models.IntegerField(
        choices=RATING_CHOICES, default=0)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def __str__(self):
        return str(self.breed) + '|' + str(self.username)

    def get_absolute_url(self):
        """ set absolute url """
        return reverse('review_list', kwargs={'pk': self.pk})


breed_review = BreedReview.objects.all()