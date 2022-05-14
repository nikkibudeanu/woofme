from django.db import models
from django.contrib.auth.models import User
import numpy as np

# Create your models here.
class Breed(models.Model):
    breed_name = models.Charfield(max_length=200)

    def average_review(self):
        all_reviews = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_reviews)

    def __unicode__(self):
        return self.name

class BreedReview(models.Model):
    ADAPTABILITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ),

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

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    published_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models. Charfield(max_length=200)
    adaptability = models.IntegerField(choices=ADAPTABILITY_CHOICES)
    friendliness = models.IntegerField(choices=FRIENDLINESS_CHOICES)
    trainability = models.IntegerField(choices=TRAINABILITY_CHOICES)
    needs = models.IntegerField(choices=HEALTH_GROOMING_NEEDS_CHOICES)