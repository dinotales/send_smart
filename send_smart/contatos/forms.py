from django import forms
from .models import Contato

class ContatoForms(forms.Form):


    nome= forms.CharField(label="Nome",widget=forms.TextInput(attrs={'class':'form=control'}))
    contato=forms.CharField(label="Contato",widget=forms.TextInput(attrs={'class':'form=control'}))
    selecionado=forms.MultipleChoiceField(label="status", widget = forms.CheckboxSelectMultiple)

