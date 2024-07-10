from django.shortcuts import render
from .forms import mensagemForms
from .models import mensagem
from contatos.models import Contato

# Create your views here.

def enviar (request):
    form= mensagemForms(request.POST)

    if form.is_valid():
        model=mensagem()
        model.texto=form.cleaned_data['texto']
        model.save()
    
    selecionados=Contato.objects.filter(enviar=True)

    for row in enumerate(selecionados):

        pessoa=row[1]

        print("Ola, "+ str(pessoa))

    

    return render (request, 'mensagem/texto.html',{'form':form})

