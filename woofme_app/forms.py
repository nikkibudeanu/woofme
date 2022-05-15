from django import forms
from .models import BreedReview

class BreedReviewForm(forms.ModelForm):
    class Meta:
        model = BreedReview
        fields =['breed', 'user_name', 'review', 'adaptability', 'friendliness', 'trainability','health_and_grooming_needs' ]

# form = BreedReview()
# breed_review = BreedReview.objects.get(pk=1)
# form = BreedReviewForm(instance=breed_review)