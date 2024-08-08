from django.urls import path
from inicio.views import inicioView

app_name='inicio'

urlpatterns=[
    path ('',inicioView, name='inicioView'),

]