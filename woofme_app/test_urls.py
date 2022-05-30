from django.test import TestCase
from .models import BreedReview


class TestUrls(TestCase):

    def setup(TestCase):
        self.review = BreedReview.objects.create(
            name= 'nametest1',
            breed_group="breed_group",
            review="test_review",
            adaptability="1",
            trainability="5",
            friendliness="3",
            health_and_grooming_needs="2",
            rating="5",
            user_name="Nikoleta")
            
    
    def test_home_page_working(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
      
      
    def test_add_review_page_working(self):
        response = self.client.get('/add_review')
        self.assertEqual(response.status_code, 301)

    def test_breed_rating_view_working(self):
        response = self.client.get('/review_list')
        self.assertEqual(response.status_code, 301)

    def test_review_page_view_working(self):
        response = self.client.get('/review_page')
        self.assertEqual(response.status_code, 301)