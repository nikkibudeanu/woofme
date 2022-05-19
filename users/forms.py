from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #first_name = forms.CharField(max_length=50(attrs={'class':'form-control'}))
    #last_name = forms.CharField(max_length=50(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwaargs)

        self.fields['username'].widget.attr['class']= 'form-control'
        self.fields['password1'].widget.attr['class']= 'form-control'
        self.fields['password2'].widget.attr['class']= 'form-control'