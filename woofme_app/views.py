from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BreedReview, Breed
from .forms import BreedReviewForm, CreateBreedGroupForm
from .models import BreedGroup

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.
class HomeView(ListView):
    """Render homepage view"""

    model = BreedReview
    template_name = 'home.html'

class AddReviewView(CreateView):
    """ Render add review page view """
    model = BreedReview
    form_class = BreedReviewForm
    template_name = 'add_review.html'


def get_review(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            form=form_class

        return render(request, 'home.html', {'form': form_class})


class BreedRatingView(ListView):
    model = BreedReview
    template_name = 'review_list.html'  

class BreedGroupCreateView(BSModalCreateView):
    template_name = 'add_review/create_group.html'
    form_class = CreateBreedGroupForm
    success_message = 'Success!'

