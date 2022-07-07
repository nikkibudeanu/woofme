""" System module """
from django.test import TestCase


class TestUrls(TestCase):
    """ test if urls are loading correctly """
    def test_home_page_working(self):
        """ test if home view loads without errors"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
   
    def test_add_review_page_working(self):
        """ test if add review page is loading without errors """
        response = self.client.get('/add_review/')
        self.assertEqual(response.status_code, 302)

    def test_breed_rating_view_working(self):
        """ test if breed rating view is loading correctly"""
        response = self.client.get('/review_list')
        self.assertEqual(response.status_code, 301)
