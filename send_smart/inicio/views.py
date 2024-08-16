from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mensagem.models import controle

# Create your views here.
@login_required(login_url='/account/login')
def inicioView(request):

    envios=controle.objects.all()

    return render (request,'inicio/indice.html',{'envios':envios})