from django.test import TestCase
from .forms import CreateBreedForm, CreateBreedGroupForm


class CreateBreedFormTest(TestCase):
    """ Test create breed form """
    def test_createbeer_form_valid(self):
        """Test if breed form is valid"""
        form = CreateBreedForm(data={
            "breed_name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_createbreed_form_is_not_valid(self):
        """ Test if Create Breed Form  is invalid"""
        form = CreateBreedForm(data={
            "breed_name": ""
        })
        self.assertFalse(form.is_valid())


