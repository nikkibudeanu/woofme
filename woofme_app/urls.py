""" Imports """
from django.urls import path, include
from .views import HomeView, BreedRatingView, AddReviewView, ReviewPageView, \
    BreedGroupCreateView, EditReviewView, DeleteReviewView, search_group_view
   ## ReviewPageView,
   # breed_group_view
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_review', AddReviewView.as_view(), name= "add_review"),
    path('review_list/', BreedRatingView.as_view(), name= "review_list"),
    path('review_list/review_page/<int:pk>', ReviewPageView.as_view(), name='review_page'),
    path('review_list/edit/<int:pk>', EditReviewView.as_view(), name='review_edit'),
    path('review_list/delete/<int:pk>', DeleteReviewView.as_view(), name='review_delete'),
    path('review_list/search_breed_groups/<str:group>', search_group_view, name='group'),
]
