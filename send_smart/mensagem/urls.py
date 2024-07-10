from django.urls import path
from mensagem.views import enviar

app_name='mensagem'

urlpatterns=[
    path ('',enviar, name='mensagem'),

]