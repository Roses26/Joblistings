from django import forms
from .models import employeePage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    """ username = forms.CharField(max_length=20)
    password = forms. """

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class LoginForm(forms.Form):
    
    class Meta:
        fields = ('username', 'password')
        
class employeePageForm(forms.ModelForm):
    """Form definition for employeePage."""
    name_of_employee = forms.CharField(help_text="Required!")
    location = forms.CharField(help_text="Required!")
    email = forms.EmailField(help_text="Required!")
    phoneNumber  = forms.CharField(help_text="Required!") 
    websiteURL  = forms.CharField(help_text="Required!") 
    publisheddate = forms.CharField(help_text="Required!") 
    description = forms.CharField(help_text="Required!") 
    class Meta:
        """Meta definition for employeePageform."""

        model = employeePage
        fields = [
            'name_of_employee',
            'location',
            'email',
            'phoneNumber',
            'websiteURL',
            'publisheddate',
            'description',
        ]

        