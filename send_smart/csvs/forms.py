from django import forms
from .models import Csv

def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Apenas arquivo CSV")

class CsvModelForm(forms.Form):
    arquivo= forms.FileField(label='',
                             widget=forms.FileInput
                             (attrs={'class':'form-control', 'accept':".csv"}),
                             validators=[validate_file_extension])
