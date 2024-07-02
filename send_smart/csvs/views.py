from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
# Create your views here.


def upload_file_view(request):
    form = CsvModelForm (request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvModelForm()
        obj= Csv.objects.get(activated=False)
        with open(obj.arquivo.path, 'r') as f:
            reader= csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    print(row)
    return render (request, 'csvs/upload.html',{'form':form})
