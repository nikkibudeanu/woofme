""" System module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BreedReview, Breed, BreedGroup


class SetupViewTestCase(TestCase):
    """ Test case to be used in all PostUpdateView view tests """
    def setUp(self):
        self.username = 'nikki'
        self.password = '123456'
        user = User.objects.create_user(
            username=self.username,
            email='nikki@gmail.com',
            password=self.password)
        self.client.login(username='nikki', password='123456')
        self.breed = Breed.objects.create(name='Breed')
        self.breed_group = BreedGroup.objects.create(breed_group='group')
        self.breed_review = BreedReview.objects.create(
            breed_group=self.breed_group,
            breed=self.breed,
            username=user,
            created_at='Nov. 24, 2021, 5:52 p.m.',
            review='Review Test',
            adaptability='5',
            trainability='3',
            friendliness='4',
            health_and_grooming_needs='5',
            rating='1')
        self.url = reverse('review_edit', kwargs={
            'pk': self.breed_review.id
        })


class BreedRatingView(SetupViewTestCase):
    """ Test Breed rating view response, correct url and template """
    def test_breed_rating_success_status_code(self):
        """ Test response on review list page by url """
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_url_by_name(self):
        """ Test response on review list page by name """
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)

    def test_breed_rating_correct_template(self):
        """ Test if review list is rendering correct template """
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_breed_rating_contains_correct_html(self):
        """ Test if review list is rendering correct html """
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, ' Latest breed Reviews')

    def test_breed_rating_does_not_contain_incorrect_html(self):
        """ Test- review list is rendering incorrect html and
        display a message """
        response = self.client.get(reverse('review_list'))
        self.assertNotContains(
                response, 'Hi there! I got lost! I should be on a different page!.')


class ReviewPageViewTests(SetupViewTestCase):
    """Test Review page view response, correct url and template """

    def test_review_page_view_url_exists(self):
        """ Test if review detail url exist """
        response = self.client.get(
            '/review_list/review_page/' + str(self.breed_review.id))
        self.assertEqual(response.status_code, 200)

    def test_review_page_success_status_code(self):
        """ Test if review page view renders correctly """
        url = reverse('review_page', kwargs={
            'pk': self.breed_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_review_page_url_by_name(self):
        """ Test if review page view render correct by name """
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_review_page_uses_correct_template(self):
        """ Test if review page view uses correct template """
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_page.html')

    def test_review_page_contains_correct_html(self):
        """ Test if review page has correct html """
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertContains(response, 'Rating')

    def test_review_page_invalid_html(self):
        """ Test if review page has wrong html and displays a message """
        response = self.client.get(reverse('review_page', kwargs={
            'pk': self.breed_review.id}))
        self.assertNotContains(
                response, 'Hi there! I got lost! I should be on a different page!.')

class AddReviewViewTest(SetupViewTestCase):
    """ Test Add review view's rendering correct url and template """
    def setUp(self):
        """Setup user SetupViewTestCase"""
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_add_review_breed_group_post(self):
        """ Login a mock user and test if add breed group is using
        correct form and post it correct """
        super().__init__()
        self.client.login(username='anna', password='12345')
        payload = {'breed_group': 'group review'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)

    def test_add_review_breed_group_form_invalid(self):
        """ Login a mock user and test if add breed group is using
        correct form and refresh page when beer style is empty """
        self.client.login(username='anna', password='12345')
        payload = {'breed_group': ''}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)

    def test_add_review_breed_name(self):
        """ Login a user and test if add breed name is using
        correct form and post it correct """
        payload = {'breed.name': 'Breed_post'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('breed_form', response.context)

    def test_add_review_breed_form_is_invalid(self):
        """ Login a user and test if add breed name is using
        correct form and refresh page when breed name is empty """
        self.client.login(username='nikki', password='12345')
        payload = {'breed.name': ''}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('breed_form', response.context)

    def test_if_add_review_breed_can_post(self):
        """ Create a  user and a review, check if review is correct post
        and redirect user """
        
        payload = {
            'breed_group': self.breed_group.id,
            'breed': self.breed.id,
            'review': 'Review from post method',
            'adaptability': '4',
            'friendliness': '4',
            'trainability': '4',
            'health_and_grooming_needs': '3',
            'rating': '1'
                    }
        response = self.client.post(reverse('add_review'), data=payload)
        self.assertEqual(response.status_code, 302)

    def test_add_review_form_invalid(self):
        """ Create a  user and a review, check if review is incorrect and
        refesh the page """
        self.client.login(username='nikki', password='12345')
        payload = { 'breed.name': ''
                    }
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('breed_form', response.context)


class EditReviewViewTest(SetupViewTestCase):
    """ Test edit review view render response """
    def setUp(self):
        """ Setup user and review from SetupViewTestCase """
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)
        
    def test_status_code(self):
        """ Test if edit view is rendering right """
        self.assertEqual(self.response.status_code, 200)


class SuccessfulEditReviewViewTests(SetupViewTestCase):
    """ Test edit review sucessfull view response """

    def setUp(self):
        """ Setup user and review """
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_review_is_updated(self):
        """ Test if update review is done correctlly and refresh db """
        self.breed_review.review = 'Test edited'
        self.breed_review.save()
        self.breed_review.refresh_from_db()
        self.assertEqual(self.breed_review.review, 'Test edited')

    def test_if_edited_review_url_renders(self):
        """ Test if edit review page renders correctly"""
        response = self.client.get(
            '/review_list/edit/' + str(self.breed_review.id))
        self.assertEqual(response.status_code, 200)

    def test_edit_review_view_success_status_code(self):
        """ Test status code of edit review page"""
        url = reverse('review_edit', kwargs={
            'pk': self.breed_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_review_url_by_name(self):
        """ Test if edit review is getting the right url by name"""
        response = self.client.get(reverse('review_edit', kwargs={
            'pk': self.breed_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_edit_review_correct_template(self):
        """ Test if edit review view uses the valid template"""
        response = self.client.get(reverse('review_edit', kwargs={
            'pk' : self.breed_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/edit_review.html')

    def test_edit_review_contains_incorrect_html(self):
        """ Test if edit review view renders the invalid template"""
        response = self.client.get(reverse('review_edit', kwargs={
            'pk': self.breed_review.id}))
        self.assertNotContains(
            response, 'Hi there! I got lost! I should be on a different page!.')
    
    def test_edit_review_contains_correct_html(self):
        """ Test if edit review view uses the valid html"""
        response = self.client.get(reverse('review_edit', kwargs={
            'pk': self.breed_review.id}))
        self.assertContains(response, 'Adaptability')


class TestSearchBreedView(SetupViewTestCase):
    """ Test if search breed views """
    def setUp(self):
        """ Setup user and review"""
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_search_breed_view_get(self):
        """ test if breed name is loading on search"""
        search = {'searched': self.breed.name}
        response = self.client.post(reverse('search_breed'), search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/search_breed.html')

    def test_search_breed_view_post(self):
        """ Test if breed name search are working in post"""
        search = {'searched': self.breed.name}
        response = self.client.post(reverse('search_breed'), search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/search_breed.html')
