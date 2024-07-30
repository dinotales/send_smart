from django import forms

class mensagemForms(forms.Form):

    texto= forms.CharField (label='',
                            widget=forms.Textarea(
                            attrs={'class':'form-control',
                                   'rows': 3
                                   }))
   
class imagemForms(forms.Form):
   
   imagem= forms.ImageField (label='',
                              widget=forms.FileInput
                              (attrs={'class':'form-control'})
                              )



