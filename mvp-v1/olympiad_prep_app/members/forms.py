# forms.py
from django import forms
from .models import Document  # Replace YourModel with your actual model name

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ('creatorId',)  # Or specify the fields you want in the form
        # Or exclude fields:
        # exclude = ('some_field',)

       