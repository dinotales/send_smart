from django.db import models

# Create your models here.

class imagem(models.Model):

    imagem=models.ImageField(upload_to='mensagem/')
    selecinar=models.BooleanField(default=False)
