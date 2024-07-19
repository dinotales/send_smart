from django.shortcuts import render, HttpResponse
from django.template import loader
from .forms import mensagemForms
from .models import mensagem
from contatos.models import Contato
from django.views.generic import ListView


# Create your views here.

def enviar (request):
    form= mensagemForms(request.POST)

    if form.is_valid():

        print(form.cleaned_data['texto']) 

    return render (request, 'mensagem/texto.html',{'form':form})



  



