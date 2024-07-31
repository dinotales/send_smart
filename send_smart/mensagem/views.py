from django.shortcuts import render, redirect
from .forms import mensagemForms, imagemForms, enviarForms
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
            delet=imagem.objects.all()
            delet.delete()
            model=imagem()
            model.imagem=form.cleaned_data.get('imagem')
            model.save()
    imagens=imagem.objects.all()        
    return render (request, 'mensagem/upload_img.html',{'form':form, 'imagens':imagens})
imagens=imagem.objects.all() 
for img in imagens:
    print(img.imagem)

def enviarImagem(request):

        x=request.session['x']
        contatos=Contato.objects.filter(id__in=x)
        imagens=imagem.objects.all()
        caminho="C:/Users/note/Desktop/teste/ilustracao.png" 
        form=enviarForms(request.POST)
        if form.is_valid():

            navegador=webdriver.Chrome()
            navegador.get('https://web.whatsapp.com/')

            while len(navegador.find_elements(By.ID, "side"))<1:
                time.sleep(1)

            for contato in contatos:
                numero=contato.contato
                link=f"https://web.whatsapp.com/send?phone={numero}"
                navegador.get(link)
                wait = WebDriverWait(navegador, 10)
                wait.until (lambda navegador: navegador.find_element(By.CSS_SELECTOR,"span[data-icon='plus']"))
                navegador.find_element(By.CSS_SELECTOR,"span[data-icon='plus']").click()
                wait = WebDriverWait(navegador, 10)
                wait.until (lambda navegador: navegador.find_element(By.CSS_SELECTOR,"input[type='file']"))
                navegador.find_element(By.CSS_SELECTOR,"input[type='file']").click()
                # wait = WebDriverWait(navegador, 10)
                # wait.until (lambda navegador: navegador.find_element(By.CSS_SELECTOR,"input[type='file']"))
                # attach.send_keys("C:/Users/note/Desktop/teste/ilustracao.png")
                # time.sleep(3)
                # navegador.find_element(By.CSS_SELECTOR,"span[data-icon='send-light']").click()

        return render (request, 'mensagem/image.html',{'form':form, 'contatos':contatos})


  



