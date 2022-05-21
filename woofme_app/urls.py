from django.urls import path, include
from .views import HomeView, BreedRatingView, AddReviewView
   ## ReviewPageView, UpdateReviewView, DeleteReviewView, \
   # breed_group_view
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_review', AddReviewView.as_view(), name= "add_review"),
    path('review_list/', BreedRatingView.as_view(), name= "review_list"),
    ##path('review_list/review_page/<int:pk>',
         #ReviewPageView.as_view(), name='review_page'),
   # path('review_list/edit/<int:pk>',
   #     UpdateReviewView.as_view(), name='review_update'),
    #path('review_list/delete/<int:pk>',
         #DeleteReviewView.as_view(), name='review_delete'),
    path('add_review/create_group', BreedGroupCreateView.as_view(), name='create_group'),
    #path('review_list/group',
        # views.breed_group_view, name='breedgroup'),

]
