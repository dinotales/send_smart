from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForms
import json

# Create your views here.


def cadastradoContatos(request):
    # contatos=Contato.objects.all()
    if request.POST:
        x=request.POST.getlist('check[]')
        print(x)
        contatos=Contato.objects.filter(id__in=x)

    else:
        contatos=Contato.objects.all()

    # print(contatos)
    return render (request,"contatos/contatos_list.html",{'contatos':contatos})

# def selecionar(request):

#     x=request.POST.getlist('check[]')
#     print(x)
#     return redirect('/',lista=x)

