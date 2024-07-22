from django.shortcuts import render
from .forms import mensagemForms
from contatos.views import selecionar
from contatos.models import Contato
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.key import Keys

# Create your views here.
def enviar (request):
    form= mensagemForms(request.POST)

    if form.is_valid():

        mensagem= form.cleaned_data['texto'] 
        x=request.session['x']
        contatos=Contato.objects.filter(id__in=x)
        print(contatos)
        navegador=webdriver.Chrome()
        navegador.get('https://web.whatsapp.com/')

        while len(navegador.find_elements(By.ID, "side"))<1:
            time.sleep(1)


    return render (request, 'mensagem/texto.html',{'form':form})    

    

  



