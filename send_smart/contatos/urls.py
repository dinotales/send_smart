from django.urls import path
from .views import cadastradoContatos,selecionar,atualizarContato,deletetarContato

app_name='contatos'

urlpatterns=[
    path('',cadastradoContatos, name='lista_contato'),
    path('selecionados',selecionar, name='lista_selecionados'),
    path('<int:id_contato>/atualizar',atualizarContato, name='atualizar_contato'),
    path('<int:id_contato>/deletar',deletetarContato, name='deletar_contato'),



]