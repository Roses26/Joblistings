from django import forms
from .models import jobs

class jobs_form(forms.ModelForm):
    """Form definition for jobs."""
    title = forms.CharField(help_text="Required!")
    location = forms.CharField(help_text="Required!")
    email = forms.CharField(help_text="Required!")
    phoneNumber = forms.CharField(help_text="Required!")
    websiteURL = forms.CharField(help_text="Required!")
    publisheddate = forms.CharField(help_text="Required!")
    description = forms.CharField(help_text="Required!")

    class Meta:
        """Meta definition for jobs_form."""

        model = jobs
        fields = [
           'title', 
           'location', 
            'email', 
            'phoneNumber', 
            'websiteURL', 
            'publisheddate', 
            'description', 

        ]

        