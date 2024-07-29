from django.urls import path
from mensagem.views import enviar, enviarImagem

app_name='mensagem'

urlpatterns=[
    path ('',enviar, name='mensagem'),
    path('imagem',enviarImagem, name='enviarImagem')
]