from django.test import TestCase
from .models import Breed, BreedGroup, BreedReview
from .forms import CreateBreedForm


class SetupClass(TestCase):
    
    def set_up(self):
        self.breed = Breed.objects.create(breed_name='nametest')
        self.breed_group = BreedGroup.objects.create(breed_group='grouptest')
        self.review = BreedReview.objects.create(review='Review test')
        self.adaptability = BreedReview.objects.create(adaptability='5')
        self.trainability = BreedReview.objects.create(trainability='5')
        self.friendliness = BreedReview.objects.create(friendliness='5')
        self.health_and_grooming_needs = BreedReview.objects.create(health_and_grooming_needs='5')
        self.rating = BreedReview.objects.create(rating='4')
        self.published_date = BreedReview.objects.create(published_date='Oct. 24, 2022, 5:46 p.m.')
        self.user_name - BreedReview.objects.create(user_name='Nikoleta')




class CreateBreedFormTest(TestCase):
    """ Test create breed form """
   
    def test_create_breed_form_valid(self):
        """Test if breed form is valid"""
        form = CreateBreedForm(data={
            "name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_create_breed_form_is_not_valid(self):
        """ Test if Create Breed Form  is invalid"""
        form = CreateBreedForm(data={
            "name": ""
        })
        self.assertFalse(form.is_valid())

    def test_create_breed_form_length(self):

        form = CreateBreedForm(data={
            "name": str('a'*300)
        })
        self.assertFalse(form.is_valid())


