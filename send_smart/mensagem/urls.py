from django.urls import path
from mensagem.views import enviar, listagem

app_name='mensagem'

urlpatterns=[
    path ('',enviar, name='mensagem'),
    path('selecionados/',listagem.as_view(), name='selecionados')

]