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

        print(model.texto) 

    return render (request, 'mensagem/texto.html',{'form':form})


def listaContato (request):
    
    contatos_selecionados= []
    telefone_selecionado=[]
    obj=Contato.objects.filter(enviar=True).values_list('nome')
    contato_selecionados=Contato.objects.filter(enviar=True).values_list('contato')

    contador=0
    for pessoa in obj:
        contatos_selecionados.append(pessoa)

        for contato in contato_selecionados:
            telefone_selecionado.append(contato)

        print("Olá, ", ''.join(contatos_selecionados[contador]).replace("'",""))
        print("Telefone: ", ''.join(telefone_selecionado[contador]).replace("'",""))
        enviar(request)
    
        contador=contador+1
        


class listagem(ListView):
    model=Contato

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        new_context = Contato.objects.filter(
            enviar=True,)
        return new_context

  



