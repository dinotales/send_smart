from django import forms
from .models import mensagem, Selecionados

class mensagemForms(forms.ModelForm):

    class Meta:
        model= mensagem

        fields= ('texto',)

class selecionadoForms(forms.ModelForm):

    class Meta:
        model= Selecionados

        fields= ('nome',)


