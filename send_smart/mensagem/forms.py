from django import forms

class mensagemForms(forms.Form):

    texto= forms.CharField (widget=forms.TextInput(attrs={'class':'form-control'}))


# class selecionadoForms(forms.ModelForm):

#     class Meta:
#         model= Selecionados

#         fields= ('nome',)


