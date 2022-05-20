from django import forms
from .models import BreedReview, BreedGroup, Breed
from bootstrap_modal_forms.forms import BSModalModelForm

class BreedReviewForm(forms.ModelForm):
    class Meta:
        model = BreedReview
        fields =['breed', 'user_name', 'review', 'adaptability', 'friendliness', 'trainability','health_and_grooming_needs', 'breed_image' ]

        widgets = {
            'review': forms.Textarea(attrs={'class' : 'form-control'})
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
        fields = '__all__'
        widgets = {
            'breed_group': forms.TextInput(attrs={
                'class': 'form-control'}),
        }
