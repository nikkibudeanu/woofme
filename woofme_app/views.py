from django.shortcuts import render, get_object_or_404
from .models import BreedReview, Breed

# Create your views here.
def home(request):

    return render(request, 'woofme_app/home.html', {})

def add_review(request):
    return render(request, 'woofme_app/add_review.html', {})

def review_list(request):
    review_list = BreedReview.objects.order_by('-published_date')[:9]
    context = {'review_list':review_list}
    return render(request, 'woofme_app/review_list.html', context)

def review_page(request, review_id):
    review = get_object_or_404(BreedReview, pk=review_id)
    return render(request, 'woofme_app/review_page.html', {'review':review})

def breed_list(request):
    breed_list = Breed.objects.order_by('-name')
    context = {'breed_list':breed_list}
    return render(request, 'woofme_app/breed_list.html', context)

def breed_page(request, breed_id):
    breed = get_object_or_404(Breed, pk=breed_id)
    return render(request, 'woofme_app/breed_page.html',{'breed':breed})