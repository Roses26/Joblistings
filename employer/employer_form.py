from django import forms
from .models import employer

class employer_form(forms.ModelForm):
    """Form definition for employer."""
    name_of_employer = forms.CharField(help_text="Required!")
    location_of_job = forms.CharField(help_text="Required!")
    email = forms.EmailField(help_text="Required!")
    phoneNumber  = forms.CharField(help_text="Required!") 
    websiteURL  = forms.CharField(help_text="Required!") 
    publisheddate = forms.CharField(help_text="Required!") 
    description = forms.CharField(help_text="Required!")

    class Meta:
        """Meta definition for employer_form."""

        model = employer
        fields = [
            'name_of_employer',
            'location_of_job',
            'email',
            'phoneNumber',
            'websiteURL',
            'publisheddate',
            'description',
        ]

        