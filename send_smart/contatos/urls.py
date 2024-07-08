from django.urls import path
from .views import listaContato

app_name='contatos'

urlpatterns=[
    path('',listaContato.as_view(), name='lista_contato'),


]