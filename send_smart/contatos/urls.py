from django.urls import path
from .views import cadastradoContatos,enviarSelecionados,atualizarContato,deletetarContato,selecionar,pesquisar

app_name='contatos'

urlpatterns=[
    path('',cadastradoContatos, name='lista_contato'),
    path('selecionados',enviarSelecionados, name='lista_selecionados'),
    path('<int:id_contato>/atualizar',atualizarContato, name='atualizar_contato'),
    path('<int:id_contato>/deletar',deletetarContato, name='deletar_contato'),
    path('selecionar', selecionar, name='selecionar'),
    path('pesquisar',pesquisar, name="pesquisar")



]