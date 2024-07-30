from django.shortcuts import render, redirect
from .forms import mensagemForms, imagemForms
from contatos.views import selecionar
from contatos.models import Contato
from mensagem.models import imagem
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
    print(form)
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

def upload_image(request):
    form= imagemForms(request.POST, request.FILES)
    if form.is_valid():
            model=imagem()
            model.imagem=form.cleaned_data.get('imagem')
            model.save()        
    return render (request, 'mensagem/upload_img.html',{'form':form})
# def enviarImagem(request):

#         x=request.session['x']
#         contatos=Contato.objects.filter(id__in=x)

#         navegador=webdriver.Chrome()
#         navegador.get('https://web.whatsapp.com/')

#         while len(navegador.find_elements(By.ID, "side"))<1:
#             time.sleep(1)

#         for contato in contatos:
#             numero=contato.contato
#             link=f"https://web.whatsapp.com/send?phone={numero}"
#             navegador.get(link)
#             wait = WebDriverWait(navegador, 10)
#             wait.until (lambda navegador: navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span'))
#             navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
#             wait = WebDriverWait(navegador, 10)
#             wait.until (lambda navegador: navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/span'))
#             attach = navegador.find_element(By.CSS_SELECTOR,"input[type='file']")
#             attach.send_keys(imagem)
#             time.sleep(3)
#             send = navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')
#             send.send_keys (Keys.ENTER)

#         return render (request, 'mensagem/image.html',{'form':form, 'contatos':contatos})


  



