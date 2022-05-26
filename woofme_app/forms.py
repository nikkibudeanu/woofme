from django import forms
from .models import BreedReview, BreedGroup, Breed
from bootstrap_modal_forms.forms import BSModalModelForm

class BreedReviewForm(forms.ModelForm):
    class Meta:
        model = BreedReview
        fields = [ 'breed', 'review','adaptability',  'trainability', 'friendliness', 'health_and_grooming_needs', 'rating']

        widgets = {
            'review': forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Go on! Write your review here!'})
        }

# form = BreedReview()
# breed_review = BreedReview.objects.get(pk=1)
# form = BreedReviewForm(instance=breed_review)


class CreateBreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }