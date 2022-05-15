from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('review_list/', views.review_list, name = "review_list"),
    path('review_list/pk:<review_id>', views.review_page, name='review_page'),
    path('breed', views.breed_list, name='breed_list'),
    path('breed/pk:<breed_id>', views.breed_page, name='breed_page'),

]
