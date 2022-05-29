from django.test import TestCase


class TestUrls(TestCase):
    
    def test_home_page_working(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
      
      
    def test_add_review_page_working(self):
        response = self.client.get('/add_review')
        self.assertEqual(response.status_code, 301)

