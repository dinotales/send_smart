from django.db import models

# Create your models here.

class imagem(models.Model):

    imagem=models.ImageField(upload_to='mensagem/')
    selecinar=models.BooleanField(default=False)

class controle (models.Model):

    mensagem=models.CharField(max_length=1000)
    img=models.ImageField(default=False)
    sucesso=models.IntegerField()
    erro=models.IntegerField()
    dataEnvio=models.DateTimeField(auto_now_add=True)