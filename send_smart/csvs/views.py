from django.shortcuts import render, redirect
from .forms import CsvModelForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from contatos.models import Contato
from django.contrib import messages

# Create your views here.


def upload_file_view(request):
    form = CsvModelForm (request.POST or None, request.FILES or None)
    try:
        if form.is_valid():        
            model=Csv()
            model.arquivo=form.cleaned_data['arquivo']
            model.nome=request.FILES ['arquivo']
            model.save()
            form= CsvModelForm()
            obj= Csv.objects.get(ativo=False)
            messages.success(request, "Arquivo cadastrado com sucesso")
            messages.get_messages(request).used=True
            with open(obj.arquivo.path, 'r') as f:
                reader= csv.reader(f)

                for i, row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        telefone= row[1]
                        pessoa=row[0]
                        Contato.objects.create(
                            nome=pessoa,
                            contato= telefone,
                        )
                obj.ativo=True
                obj.save()
    
        return render (request, 'csvs/upload.html',{'form':form})
    except:
            messages.error(request, "Já existe esse arquivo cadastrado")
            messages.get_messages(request).used=True
            return redirect("/")