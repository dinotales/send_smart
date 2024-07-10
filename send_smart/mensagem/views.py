from django.shortcuts import render, HttpResponse
from django.template import loader
from .forms import mensagemForms
from .models import mensagem,Selecionados
from contatos.models import Contato
from django.views.generic import ListView


# Create your views here.

def enviar (request):
    form= mensagemForms(request.POST)

    if form.is_valid():
        model=mensagem()
        model.texto=form.cleaned_data['texto']
        selecionados=Contato.objects.filter(enviar=True)

        for row in enumerate(selecionados):

            pessoa=row[1]

            print("Ola, "+ str(pessoa))
            print(model.texto) 

    return render (request, 'mensagem/texto.html',{'form':form})


class listaContato (ListView):
    nome_selecionados=Contato.objects.filter(enviar=True).values_list('nome')
    contato_selecionados=Contato.objects.filter(enviar=True).values_list('contato')
    
    

    for selecionado in enumerate(nome_selecionados):
            
            pessoa=selecionado[1]
            Selecionados.objects.create(
                nome=pessoa,
            )
                 

    model= Selecionados

  



