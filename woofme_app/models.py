from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import numpy as np

# Create your models here.
class Breed(models.Model):
    breed_name = models.CharField(max_length=200)

    def average_review(self):
        all_ratings= map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.breed_name

class BreedReview(models.Model):
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

    HEALTH_GROOMING_NEEDS_CHOICES=(
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

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    breed_image = CloudinaryField('image', default='placeholder')
    published_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    adaptability = models.IntegerField(choices=ADAPTABILITY_CHOICES)
    friendliness = models.IntegerField(choices=FRIENDLINESS_CHOICES)
    trainability = models.IntegerField(choices=TRAINABILITY_CHOICES)
    health_and_grooming_needs = models.IntegerField(choices=HEALTH_GROOMING_NEEDS_CHOICES)
    # rating = models.IntegerField(choices=RATING_CHOICES)