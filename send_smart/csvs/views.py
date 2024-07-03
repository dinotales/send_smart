from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
# Create your views here.


def upload_file_view(request):
    form = CsvModelForm (request.POST or None, request.FILES or None)
    if form.is_valid():
        model=Csv()
        model.arquivo=form.cleaned_data['arquivo']
        model.nome=request.FILES ['arquivo']
        model.save()
        form=CsvModelForm()
        # print(request.FILES ['arquivo'])
        name=request.FILES ['arquivo']
        obj= Csv.objects.get(ativo=False,nome=name)
        with open(obj.arquivo.path, 'r') as f:
            reader= csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    print(row)
    return render (request, 'csvs/upload.html',{'form':form})

