from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForms
import json

# Create your views here.


def cadastradoContatos(request):
    contatos=Contato.objects.all()

    return render (request,"contatos/contatos_list.html",{'contatos':contatos})

def selecionar(request):

    if request.method== 'POST':
        x=request.POST.getlist('check[]')
        print(x)

    # check= request.POST.getlist('checks[]')
    # print(check)  

    return render (request,"contatos/contatos_list.html")

