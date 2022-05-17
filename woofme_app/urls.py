from django.urls import path, include
from .views import HomeView, BreedRatingView, AddReviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('rate/<int:pk>', BreedRatingView.as_view(), name = "breed_rate"),
    path('add_review', AddReviewView.as_view(), name = "add_review"),
    #path('review_list/pk:<review_id>', views.review_page, name='review_page'),
    #path('breed', views.breed_list, name='breed_list'),
    #path('breed/pk:<breed_id>', views.breed_page, name='breed_page'),

]
