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

        