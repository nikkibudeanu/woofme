"""Imports"""
from cloudinary.forms import CloudinaryFileField
from django import forms
from .models import BreedReview, Breed
# from bootstrap_modal_forms.forms import BSModalModelForm


class BreedReviewForm(forms.ModelForm):
    """ Create form to add a new breed review"""
    class Meta:
        """ Create a breed model, choose field to display and add widget
        with bootstrap class"""
        model = BreedReview
        fields = [
            'breed',
            'review',
            'adaptability',
            'trainability',
            'friendliness',
            'health_and_grooming_needs',
            'rating']

        widgets = {
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Go on! Write your review here!'})
        }


class CreateBreedForm(forms.ModelForm):
    """ Create Breed Form"""
    class Meta:
        """ Get breed group model, choose field to display and
        add widget with bootstrap class"""
        model = Breed
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
