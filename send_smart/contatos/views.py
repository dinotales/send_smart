from django.shortcuts import render, redirect
from .models import Contato
from .forms import atualizarForms


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
    
def atualizarContato(request,id_contato):
    if request.POST:

        form=atualizarForms(request.POST)
        if form.is_valid():
            model=to_model(form)

            Contato.objects.filter(pk=id_contato).update(
                nome=model.nome,
                contato=model.contato
            )
            return redirect('/contato')
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