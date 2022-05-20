from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BreedReview, Breed
from .forms import BreedReviewForm


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

    def get_absolute_url(self):
        return reverse('home')


class BreedRatingView(ListView):
    model = BreedReview
    template_name = 'review_list.html'


# def review_list(request):
#     review_list = BreedReview.objects.order_by('-pub_date')[:9]
#     context = {'review_list':review_list}
#     return render(request, 'review_list.html', context)


# def review_page(request, review_id):
#     review = get_object_or_404(BreedReview, pk=review_id)
#     return render(request, 'reviews/review_list.html', {'review': review})


# def breed_list(request):
#     breed_list = Breed.objects.order_by('-name')
#     context = {'breed_list':breed_list}
#     return render(request, 'reviews/breed_list.html', context)


# def breed_page(request, breed_id):
#     breed = get_object_or_404(Breed, pk=breed_id)
#     return render(request, 'reviews/breed_detail.html', {'breed': breed})