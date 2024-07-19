from django.urls import path
from .views import cadastradoContatos,selecionar
from mensagem.views import enviar

app_name='contatos'

urlpatterns=[
    path('',cadastradoContatos, name='lista_contato'),
    path('selecionados',selecionar, name='lista_contato'),



]