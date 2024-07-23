from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Contato
from .forms import ContatoForms
from mensagem.forms import mensagemForms
import json

# Create your views here.


def cadastradoContatos(request):
    # contatos=Contato.objects.all()
    # if request.POST:
    #     x=request.POST.getlist('check[]')
    #     print(x)
    #     contatos=Contato.objects.filter(id__in=x)
    #     return render (request,"contatos/selecionados_list.html",{'contatos':contatos})

    # else:
    contatos=Contato.objects.all()

    # print(contatos)
    return render (request,"contatos/contatos_list.html",{'contatos':contatos})

def selecionar(request):
    if request.POST:
        x= request.POST.getlist('check[]')
        # print(x)
        contatos=Contato.objects.filter(id__in=x)
        request.session ['x']=x
    
    return redirect ("http://127.0.0.1:8000/mensagem")
