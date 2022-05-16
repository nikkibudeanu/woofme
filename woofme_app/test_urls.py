from django.test import TestCase
from django.urls import reverse, resolve 


class test_urls(TestCase):

    def test_home_page_working(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_add_review_page_working(self):
        response = self.client.get('/add_review')
        self.assertEquals(response.status_code, 200)

