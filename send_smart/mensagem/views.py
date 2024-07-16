from django.shortcuts import render, HttpResponse
from django.template import loader
from .forms import mensagemForms, selecionadoForms
from .models import mensagem,Selecionados
from contatos.models import Contato
from django.views.generic import ListView


# Create your views here.

def enviar (request):
    form= mensagemForms(request.POST)

    if form.is_valid():

        print(form.cleaned_data['texto']) 

    return render (request, 'mensagem/texto.html',{'form':form})


  



