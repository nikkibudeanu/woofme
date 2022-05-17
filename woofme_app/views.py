from django.shortcuts import render, get_object_or_404
from .models import BreedReview, Breed
from .forms import BreedReviewForm
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class HomeView(ListView):
    model = BreedReview
    template_name = 'home.html'



class AddReviewView(CreateView):
    model = BreedReview
    template_name = 'add_review.html'
    fields = '__all__'
    def get_absolute_url(self):
        return reverse('home')


class BreedRatingView(DetailView):
    model = BreedReview
    queryset = BreedReview.objects.order_by("-published_date")
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