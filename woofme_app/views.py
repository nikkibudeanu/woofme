"""System module"""
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView, DetailView, View, UpdateView, \
    DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BreedReview, BreedGroup
from .forms import BreedReviewForm, CreateBreedForm


class HomeView(ListView):
    """Render homepage view"""
    model = BreedReview
    template_name = 'home.html'


class AddReviewView( LoginRequiredMixin, View):
    """ Render add review page view """
    template_name = 'add_review.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    

    def get_object(self):
        """ Get objects from breed review model"""
        obj = BreedReview.objects.all()
        return obj


    def get_context_data(self, **kwargs):
        """ Get the right form """
        kwargs['review'] = self.get_object()
        if 'review_form' not in kwargs:
            kwargs['review_form'] = BreedReviewForm()
        if 'breed_form' not in kwargs:
            kwargs['breed_form'] = CreateBreedForm()
        return kwargs
    
    
    def get(self, request):
        """ return to add breed form page after creating a breed"""
        return render(request, self.template_name, self.get_context_data())
        
    def post(self, request):
        """ validate data in the add review forms"""
        ctxt = {}
        if 'review' in request.POST:
            review_form = BreedReviewForm(request.POST, request.FILES)
            
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.username = request.user
                review.save()
                return redirect('review_page', review.pk)
            else:
                ctxt['review_form'] = review_form
        
        elif 'name' in request.POST:
            breed_form = CreateBreedForm(request.POST)
            if breed_form.is_valid():
                messages.success(request, 'Breed has been added.')
                breed_form.save()
            else:
                ctxt['breed_form'] = breed_form
    
        return render(request, self.template_name, self.get_context_data(**ctxt))


class BreedRatingView(ListView):
    model = BreedReview
    template_name = 'review_list.html'
    paginate_by = 6

class ReviewPageView(DetailView):
    model = BreedReview
    template_name = 'review_list/review_page.html'


class EditReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Update a  breed review after editing """
    model = BreedReview
    form_class = BreedReviewForm
    template_name = 'review_list/edit_review.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

    def __init__(self):
        self.updform = None

    def form_valid(self, form):
        """  Validate update review form and save it """
        self.updform = form.save(commit=False)
        self.slug = self.updform.breed_group
        self.updform.save()
        return redirect('review_page', self.updform.pk)


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a breed review form """
    model = BreedReview
    form_class = BreedReviewForm
    template_name = 'review_list/delete_review.html'
    success_url = reverse_lazy('review_list')
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user

def search_group_view(request, group):
    """ Define a breed group view on search """
    breed_group_reviews = BreedReview.objects.filter(slug=group).order_by('-created_at')
    return render(request, 'review_list/search_breed_groups.html', {
        'group': group, 'breed_group_reviews': breed_group_reviews})

def cat_style_menu_on_all_pages(_request):
    return{'cat_style_menu': BreedGroup.objects.all().order_by('breed_group')}


def search_breed_view(request):
    """Define a breed view search in all pages"""
    if request.method == "POST":
        searched = request.POST['searched']
    elif request.method == "GET":
        searched = request.GET['searched']


    breeds = BreedReview.objects.filter(
        breed__name__icontains=searched).order_by('-created_at')

    paginator = Paginator(breeds, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'review_list/search_breed.html', {
        'searched': searched, 'breed_review': page_obj})