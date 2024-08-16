from django.urls import path, re_path
from mensagem.views import enviarTexto, upload_image, enviarImagem
from django.views.static import serve
from django.conf import settings

app_name='mensagem'

urlpatterns=[
    path ('',enviarTexto, name='mensagem'),
    path('upload',upload_image, name='uploadImagem'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('imagem',enviarImagem, name='enviarImagem'),
]