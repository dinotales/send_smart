from django import forms

class mensagemForms(forms.Form):

    texto= forms.CharField (label='',
                            widget=forms.Textarea(
                            attrs={'class':'form-control',
                                   'rows': 3
                                   }))



