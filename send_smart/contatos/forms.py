from django import forms
from .models import Contato

class ContatoForms(forms.ModelForm):

    class Meta:
        model= Contato,
        fields= ('nome','contato')

