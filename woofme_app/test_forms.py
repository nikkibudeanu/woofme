from django.test import TestCase
from .models import Breed, BreedGroup
from .forms import CreateBreedForm


class SetupClass(TestCase):
    
    def set_up(self):
        self.breed = Breed.objects.create(breed_name='nametest')
        self.breed_group = BreedGroup.objects.create(breed_group='grouptest')


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


