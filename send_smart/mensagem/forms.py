from django import forms
from .models import mensagem

class mensagemForms(forms.ModelForm):

    class Meta:
        model= mensagem

        fields= ('texto',)

