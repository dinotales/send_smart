from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def cadastro(request):
    if request.method =="GET":
        return render(request, 'login/cadastro.html')
    else:
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha=request.POST.get('senha')

        user=User.objects.filter(username=username).first()

        if user:
        
            messages.error(request, "Já usuário com o mesmo nome")
            return render(request, 'login/cadastro.html')
        else:
            user =User.objects.create_user(username=username, email=email, password=senha)
            user.save()

            return redirect('http://127.0.0.1:8000')

def loginView(request):
    
    if request.method=="POST":
        
        username=request.POST.get('username')
        senha=request.POST.get('senha')

        user=authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return render(request, 'inicio/indice.html')
        else:
            messages.info(request, 'Usuário ou senha incorreto')
            return redirect('http://127.0.0.1:8000/account/login')
    else:
        return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000')