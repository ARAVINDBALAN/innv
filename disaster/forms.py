from django import forms 
from .models import *


class Help_form(forms.ModelForm):
    class Meta:
        model = Help
        fields = ['name','photo','location']


from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    #USERNAME_FIELD = 'email'
    class Meta:
        model = User
        fields = ('phone','email','first_name','last_name','avatar','password1','password2')


