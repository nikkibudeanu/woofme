from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'woofme_app/home.html', {})

def add_review(request):
    return render(request, 'add_review.html', {})