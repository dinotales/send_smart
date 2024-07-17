from django import forms
from .models import Csv

class CsvModelForm(forms.Form):
    arquivo= forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

    # class Meta:
    #     model = Csv
    #     fields=('arquivo', )