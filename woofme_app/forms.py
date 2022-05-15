from django import forms
form .models import BreedReview

class BreedReviewForm(forms.ModelForm):
    class Meta:
        model = BreedReview
        fields =['breed', 'user_name', 'review', 'adaptability', 'friendliness', 'trainability','health_and_grooming_needs'  ]