from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View
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

class AddReviewView(View):
    """ Render add review page view """
    template_name = 'add_review.html'


def get_object(self):
    try:
        obj = BreedReview.objects.all()
    except BreedReview.DoesNotExist:
        raise Http404('Breed Review not found!')
    return obj

def get_context_data(self, **kwargs):
    kwargs['review'] = self.get_object()
    if 'review_form' not in kwargs:
        kwargs['review_form'] = BreedReviewForm()
    if 'group_form' not in kwargs:
        kwargs['group_form'] = CreateBreedGroupForm()

    return kwargs

def get(self, request, *args, **kwargs):
    return render(request, self.template_name, self.get_context_data())

def post(self, request, *args, **kwargs):
    ctxt = {}

    if 'review' in request.POST:
        review_form = BreedReviewForm(request.POST)

        if review_form.is_valid():
            review_form.save()
        else:
            ctxt['review_form'] = review_form
    
    elif 'breed_group' in request.POST:
        group_form = CreateBreedGroupForm(request.POST)

        if group_form.is_valid():
            group_form.save()
        else:
            ctxt['group_form'] = group_form

    return render(request, self.template_name, self.get_context_data(**ctxt))

class BreedRatingView(ListView):
    model = BreedReview
    template_name = 'review_list.html'  

class BreedGroupCreateView(BSModalCreateView):
    template_name = 'add_review/create_group.html'
    form_class = CreateBreedGroupForm
    success_message = 'Success!'

