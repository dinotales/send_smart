from django.urls import path
from csvs.views import upload_file_view

app_name='csvs'

urlpatterns=[
    path ('',upload_file_view, name='upload-view'),
    # path('contato',listaContato.as_view(), name='lista_contato')


]