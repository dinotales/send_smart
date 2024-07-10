from django.shortcuts import render
from django.views.generic import ListView
from .models import Contato

# Create your views here.


class listaContato(ListView):
     model=Contato