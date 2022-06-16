""" System module """
from django.test import TestCase
from .forms import CreateBreedForm


class CreateBreedFormTest(TestCase):
    """ Test create breed form """

    def test_create_breed_form_valid(self):
        """Test if breed form is valid"""
        form = CreateBreedForm(data={
            "name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_create_breed_form_is_not_valid(self):
        """ Test if Create Breed Form  is invalid/empty"""
        form = CreateBreedForm(data={
            "name": ""
        })
        self.assertFalse(form.is_valid())

    def test_create_breed_form_length(self):
        """ Test if the name is too long """
        form = CreateBreedForm(data={
            "breed_name": str('a'*300)
        })
        self.assertFalse(form.is_valid())

