from django.contrib.auth.models import User
from django import forms 


class SignupForm(forms.Form):
    username = forms.CharField(lavel='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter Email')
    password1 = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)

   
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwaargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def unique_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists!")
        return username

    def unique_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filet(email=email)
        if r.count():
            raise ValidationError("Email already exists!")
        return email

    def same_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match!")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email']
            self.cleaned_data['password1']
        )
        return user
