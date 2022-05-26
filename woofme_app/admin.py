"""Imports"""
from django.contrib import admin
from .models import BreedGroup, Breed, BreedReview

# Register your models here.


class BreedReviewAdmin(admin.ModelAdmin):
    """ Create admin panel to view breed_reviews """
    model = BreedReview
    list_display = (
        'breed_group',
        'breed',
        'user_name',
        'review',
        'published_date')
    list_filter = ['published_date', 'user_name']
    search_fields = ['breed', 'review']


admin.site.register(BreedGroup)
admin.site.register(Breed)
admin.site.register(BreedReview)
