from django.shortcuts import render, redirect
from .models import Contato
from .forms import atualizarForms
from django.http import HttpResponse


# Create your views here.


def cadastradoContatos(request):

        contatos=Contato.objects.all()

        context = {"resultados": contatos, 'contatos':contatos} 

        return render (request,"contatos/contatos_list.html", context)

    

def enviarSelecionados(request):
    if request.POST:
        if 'texto' in request.POST:
            return redirect ("http://127.0.0.1:8000/mensagem")
        if 'imagem' in request.POST:
            return redirect ("http://127.0.0.1:8000/mensagem/upload")
    
def selecionar(request):
    if request.POST:
        x= request.POST.getlist('check[]')
        print(x)
        request.session ['x']=x
    return redirect ("http://127.0.0.1:8000/contato")
    
def atualizarContato(request,id_contato):
    if request.POST:

        form=atualizarForms(request.POST)
        if form.is_valid():
            model=to_model(form)

            Contato.objects.filter(pk=id_contato).update(
                nome=model.nome,
                contato=model.contato
            )
            return HttpResponse(status=204)
    contato=Contato.objects.get(pk=id_contato)
    form=atualizarForms(initial=
                        {'nome':contato.nome,
                        'contato':contato.contato,
                        })
    return render(request,"contatos/atualizar.html",{"form":form})

def to_model(form):
    model=Contato()
    model.nome=form.cleaned_data ['nome']
    model.contato=form.cleaned_data['contato']
    
    return model


def deletetarContato(request,id_contato):
        pessoa=Contato.objects.get(pk=id_contato)
        pessoa.delete()
        return redirect('/contato')

def pesquisar(request):
     pesquisa=Contato.objects.filter(nome__icontain='pesquisa')