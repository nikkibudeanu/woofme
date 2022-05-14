from django.shortcuts import render, get_object_or_404
from .models import BreedReview, Breed

# Create your views here.
def home(request):

    return render(request, 'woofme_app/home.html', {})

def add_review(request):
    return render(request, 'add_review.html', {})

def review_list(request):
    updated_review_list = Review.objects.order_by('-published_date')[:9]
    context = {'updated_review_list':updated_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_page(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_page.html', {'review':review})

def breed_list(request):
    breed_list = Breed.objects.order_by('-name')
    context = {'breed_list':breed_list}
    return render(request, 'reviews/breed_list.html', context)

def breed_page(request, breed_id):
    breed = get_object_or_404(Breed, pk=breed_id)
    return render(request, 'reviews/breed_page.html',{'breed':breed})