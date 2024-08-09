from django import forms

class mensagemForms(forms.Form):

    texto= forms.CharField (label='',
                            widget=forms.Textarea(
                            attrs={'class':'form-control',
                                   'rows': 3
                                   }))
   
class imagemForms(forms.Form):
   
   imagem= forms.ImageField (label='Corfimar imagem',
                              widget=forms.FileInput
                              (attrs={'class':'form-control'})
                              )


class enviarForms(forms.Form):

    enviar=forms.BooleanField(label='Certeza que deseja enviar')