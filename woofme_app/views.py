"""System module"""
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View, UpdateView, \
    DeleteView
from .models import BreedReview, BreedGroup
from .forms import BreedReviewForm, CreateBreedForm
# from django.views import generic
from django.urls import reverse_lazy
import logging
# from bootstrap_modal_forms.generic import BSModalCreateView


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
    if 'breed_form' not in kwargs:
        kwargs['breed_form'] = CreateBreedForm()

    return kwargs


def get(self, request, *args, **kwargs):
    return render(request, self.template_name, self.get_context_data())


def post(self, request, *args, **kwargs):
    ctxt = {}

    if 'review' in request.POST:
        review_form = BreedReviewForm(request.POST, request.FILES)
        logging.debug('post - review')

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user_name = request.user
            review.save()
            logging.debug('post - review - save')
            return redirect('review_page', review_pk)
        else:
            ctxt['review_form'] = review_form
    

    
    elif 'name' in request.POST:
        breed_form = CreateBreedForm(request.POST)

        if breed_form.is_valid():
            breed_form.save()
        else:
            ctxt['breed_form'] = breed_form
    
    return render(request, self.template_name, self.get_context_data(**ctxt))


class BreedRatingView(ListView):
    model = BreedReview
    template_name = 'review_list.html'
    paginate_by = 3


class BreedGroupCreateView(ListView):
    """ Create a breed group on add review page """
    template_name = 'add_review/create_breed_group.html'


class ReviewPageView(DetailView):
    model = BreedReview
    template_name = 'review_list/review_page.html'


class EditReviewView(UpdateView):
    model = BreedReview
    form_class = BreedReviewForm
    template_name = 'review_list/edit_review.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect ('review_page', self.object.pk)


class DeleteReviewView(DeleteView):
    model = BreedReview
    form_class = BreedReviewForm
    template_name = 'review_list/delete_review.html' 
    succes_url = reverse_lazy('review_list')

def group_view(request, group):
    """ Define a breed group view on search """
    group_reviews = BreedReview.objects.filter(slug=group).order_by('-published_date')
    return render(request, 'review_list/breed_groups.html', {
        'group': group, 'group_reviews': group_reviews
    })


def breed_group_list(request):
    cat_style_menu=BreedGroup.objects.all
    return render(request, 'base.html', {'cat_style_menu': cat_style_menu})

def cat_style_menu_on_all_pages(request):
    return{'cat_style_menu': BreedGroup.objects.all()}