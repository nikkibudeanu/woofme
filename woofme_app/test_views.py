""" System module"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedReview, Breed, BreedGroup


class SetupViewTestCase(TestCase):
    """ Test case for all view tests"""
    def setUp(self):
        self.breed = Breed.objects.create(name='Breed')
        self.breed_group = BreedGroup.objects.create(breed_group= 'group')
        self.breed_review = BreedReview.objects.create(
            breed_group=self.breed_group,
            breed=self.breed,
            user_name=user,
            published_date='Oct. 25, 2021, 9:45 p.m.',
            review='Review test',
            adaptability='5',
            trainability='5',
            friendliness='5',
            health_and_grooming_needs='5',
            rating='5')
        self.url = reverse('edit_review', kwargs={
            'pk': self.breed_review.id
        })

class BreedRatingView(SetupViewTestCase):
    """ Test Breed Rating view response, if correct url and template"""
    def test_breed_rating_view_success_status_code(self):
        """ Test review list page url """
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_view_by_name(self):
        """ Test review list page by name"""
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_view_if_correct_template(self):
        """ Test if review list is rendering correct template """
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_breed_rating_view_incorrect_html(self):
        """ Test if the review list is rendering the wrong html and display message if it is"""
        response = self.client.get(reverse('review_list'))
        self.assertNotContains(response, 'Hello friend! I am on the wrong page!')

    def test_breed_rating_view_valid_html(self):
        """ Test if the review list is showing the correct html"""
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, 'Latest Reviews of your favorite breeds!')


class ReviewPageViewTests(SetupViewTestCase):
    """ Test review detail view """
    
    def test_review_page_view_url_exists(self):
        """ Test if the review page view exists"""
        response = self.client.get(
            '/review_list/review_page/' + str(self.breed_review.id))
        self.assertEqual(response.status_code, 200)

    def test_review_page_success_status_code(self):
        """ Test if review page is rendering correctly"""
        url = reverse('review_page', kwargs={
            'pk':self.breed_review.id
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_review_page_url_by_name(self):
        """ Test if review page is rendering correctly by name"""
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_review_page_if_uses_correct_template(self):
        """ Test review page if it is using the correct template"""
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_page.html')

    def test_review_page_contains_wrong_html(self):
        """ Test if review page contains the wrong html and display a message if it is"""
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertNotContains(
            response, 'Hello friend! I am on the wrong page!')

    def test_review_page_view_contains_valid_html(self):
        """ Test of review page has the correct html displayed"""
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertContains(response, 'Rating')


class AddReviewViewTest(SetupViewTestCase):
    """ Test add review page response, url and template"""
    def setUp(self):
        """ Setup user and review """
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_add_review_breed_name_post(self):
        """ Login a mock user and test if add vreed name is using the valid form and posts it correctly"""
        payload = {'breed_name': ''}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('breed_form', response.context)

    def test_if_add_review_breed_can_post(self):
        """ Create a user and a review and check if review is correct"""

        payload = {
            'breed_group': self.breed_group.id,
            'breed': self.breed.id,
            'review': 'Review',
            'adaptability': '4',
            'trainability': '5',
            'friendliness': '4',
            'health_and_grooming_needs': '5',
            'rating': '3'
        }
        response = self.client.post(reverse('add_review'), data=payload)
        self.assertEqual(response.status_code, 302)


    def test_if_add_review_form_is_not_valid(self):
        """ create user and add review to check if the review is not correct"""
        self.client.login(username='fernanda', password='123456')
        payload = {
            'breed_group': self.breed_group.id,
            'breed': self.breed.id,
            'review': 'Review',
            'adaptability': '4',
            'trainability': '5',
            'friendliness': '4',
            'health_and_grooming_needs': '5',
            'rating': '3'
        }
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('review_form', response.context)


class EditViewTests(SetupViewTestCase):
    """ Test edit review view render response"""
    def setUp(self):
        """ Setup user and review """
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

        def test_status_code(self):
            """ Test if edit review is rendering correctly"""
            self.assertEqual(self.response.status_code, 200)

class SuccesfulEditReviewViewTest(SetupViewTestCase):
    """ Test edit review successful response"""

    def setUp(self):
        """ Setup user and review"""
        super().setUp()
        self.client.login(username=self.username, password=self.password)


    def test_if_review_changed(self):
        """ Test if edit review is done correctly and database is refreshed"""
        self.breed_review.review='review'
        self.breed_review.save()
        self.breed_review.refresh_from_db()
        self.assertEqual(self.breed_review.review, 'review test edited')


    def test_if_edited_review_url_created(self):
        """ Test if edit review page is rendering correctly"""
        response = self.client.get(
            '/review_list/edit/' + str(self.breed_review.id))
        self.assertEqual(response.status_code, 200)

    def test_if_edit_review_view_succes_status_code(self):
        """ Test status code for edit review page"""
        url = reverse('edit_review', kwargs={
            'pk': self.breed_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_review_url_by_name(self):
        """ Test if edit review is rendering the correct url"""
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_edit_review_correct_template(self):
        """ Test if edit review page is using the correct template"""
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/edit_review.html')


    def test_edit_review_correct_html(self):
        """ Test if edit review view is rendering the correct html"""
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.breed_review.id}))
        self.assertContains(response, 'Adaptability')

    def test_edit_review_incorrect_html(self):
        """ Test if edit review view is rendering the invalid html and display message"""
        response = self.client.get(reverse('edit_review', kwargs={
            'pk': self.breed_review.id}))
        self.assertNotContains(response, 'Hello friend! I am on the wrong page!')

