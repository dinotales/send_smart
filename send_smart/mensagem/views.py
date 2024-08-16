from django.shortcuts import render, redirect
from .forms import mensagemForms, imagemForms, enviarForms
from contatos.views import selecionar
from contatos.models import Contato
from mensagem.models import imagem, controle
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from django.contrib import messages
# import math

# Create your views here.
def enviarTexto (request):
    form= mensagemForms(request.POST)
    x=request.session['x']
    contatos=Contato.objects.filter(id__in=x)
    sucessoText=0
    erroText=0


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
            try:
                navegador.get(link)
                while len(navegador.find_elements(By.ID, "side"))<1:
                    time.sleep(1)
                wait = WebDriverWait(navegador, 10)
                wait.until (lambda navegador: navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p[1]'))
                input=navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p[1]')
                input.send_keys (Keys.ENTER)
                time.sleep(10)
                sucessoText=sucessoText+1
            except:
                erroText=erroText+1
                pass
        
        messages.info(request, 'Mensagem enviadas')

        model= controle()
        model.mensagem=form.cleaned_data ['texto']
        model.sucesso=sucessoText
        model.erro=erroText
        model.save()


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
        sucessoImg=0
        erroImg=0
        ImgEnvio="Envio de Imagem"
        if form.is_valid():

            navegador=webdriver.Chrome()
            navegador.get('https://web.whatsapp.com/')


            while len(navegador.find_elements(By.ID, "side"))<1:
                time.sleep(1)

            for contato in contatos:
                numero=contato.contato
                link=f"https://web.whatsapp.com/send?phone={numero}"
                try:
                    navegador.get(link)
                    wait = WebDriverWait(navegador, 10)
                    wait.until (lambda navegador: navegador.find_element(By.CSS_SELECTOR,"span[data-icon='plus']"))
                    navegador.find_element(By.CSS_SELECTOR,"span[data-icon='plus']").click()
                    anexar=navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
                    anexar.send_keys("/home/tsuyoshi/code/ilustracao.png")
                    wait =WebDriverWait(navegador, 10)
                    wait.until(lambda navegador: navegador.find_element(By.CSS_SELECTOR,"span[data-icon='send']"))
                    navegador.find_element(By.XPATH, '//span[@data-icon="send"]').click()
                    time.sleep(5)
                    sucessoImg=sucessoImg+1
                except:
                    erroImg=erroImg+1
                    pass
            messages.info(request, 'Mensagem enviadas')

            model= controle()
            model.mensagem=ImgEnvio
            # model.img=form.cleaned_data ['img']
            model.sucesso=sucessoImg
            model.erro=erroImg
            model.save()
                    

        return render (request, 'mensagem/image.html',{'form':form, 'contatos':contatos})


  



