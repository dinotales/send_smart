from django import forms

class mensagemForms(forms.Form):

    texto= forms.CharField (label='',
                            widget=forms.TextInput
                            (attrs={'class':'form-control'}))



