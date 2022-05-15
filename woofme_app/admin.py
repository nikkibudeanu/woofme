from django.contrib import admin
from .models import Breed, BreedReview

# Register your models here.

class BreedReviewAdmin(admin.ModelAdmin):
    model = BreedReview
    list_display = ('breed', 'user_name', 'review', 'published_date')
    list_filter = ['published_date', 'user_name']
    search_fields = ['breed','review']

admin.site.register(Breed)
admin.site.register(BreedReview, BreedReviewAdmin)

