from django.urls import path
from .views import cadastradoContatos,selecionar

app_name='contatos'

urlpatterns=[
    path('',cadastradoContatos, name='lista_contato'),
    path('selecionados',selecionar, name='lista_contato'),



]