from django.shortcuts import render
from .forms import mensagemForms
from contatos.views import selecionar
from contatos.models import Contato
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
# import math

# Create your views here.
def enviar (request):
    form= mensagemForms(request.POST)
    x=request.session['x']
    contatos=Contato.objects.filter(id__in=x)

    if form.is_valid():

        mensagem= form.cleaned_data['texto'] 
        navegador=webdriver.Chrome()
        navegador.get('https://web.whatsapp.com/')

        while len(navegador.find_elements(By.ID, "side"))<1:
            time.sleep(1)

        for contato in contatos:
            pessoa=contato.nome
            numero=contato.contato
            texto= urllib.parse.quote(f"*Olá, {pessoa}!*\n\n Tudo bem?\n {mensagem}")
            link=f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
            navegador.get(link)
            while len(navegador.find_elements(By.ID, "side"))<1:
                time.sleep(1)
            wait = WebDriverWait(navegador, 10)
            wait.until (lambda navegador: navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p[1]'))
            input=navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p[1]')
            input.send_keys (Keys.ENTER)
            time.sleep(10)


    return render (request, 'mensagem/texto.html',{'form':form, 'contatos':contatos})    

    

  



