from django import forms
from .models import BreedReview, BreedGroup, Breed
from bootstrap_modal_forms.forms import BSModalModelForm

class BreedReviewForm(forms.ModelForm):
    class Meta:
        model = BreedReview
        fields = ['breed_group', 'breed', 'review','adaptability',  'trainability', 'friendliness', 'health_and_grooming_needs', 'breed_image', 'rating']

        widgets = {
            'review': forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Go on! Write your review here!'})
        }

# form = BreedReview()
# breed_review = BreedReview.objects.get(pk=1)
# form = BreedReviewForm(instance=breed_review)

class CreateBreedGroupForm(forms.ModelForm):
    """ Create a BreedGroup Form """
    class Meta:
        """Get breed model, choose field to display and add widget
        with bootstrap class"""
        model = BreedGroup
        fields = ['breed_group']
        widgets = {
            'breed_group': forms.TextInput(attrs={
                'class': 'form-control'}),
        }

class CreateBreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['breed_name']

        widgets = {
            'breed_name' : forms.TextInput(attrs={'class':'form-control'})
        }