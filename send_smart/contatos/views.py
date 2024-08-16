from django.shortcuts import render, redirect
from .models import Contato


# Create your views here.


def cadastradoContatos(request):

    contatos=Contato.objects.all()

    return render (request,"contatos/contatos_list.html",{'contatos':contatos})

def selecionar(request):
    if request.POST:
        x= request.POST.getlist('check[]')
        request.session ['x']=x
    if 'texto' in request.POST:
        return redirect ("http://127.0.0.1:8000/mensagem")
    if 'imagem' in request.POST:
        return redirect ("http://127.0.0.1:8000/mensagem/upload")

