from django.db import models

# Create your models here.

class mensagem (models.Model):

    texto= models.CharField (max_length=500)
    ativo= models.BooleanField(default=False)

# class Selecionados(models.Model):
#     nome= models.CharField(max_length=100, unique=False)
#     contato=models.CharField(max_length=20)
#     # gestor= models.ForeignKey(User, on_delete=models.CASCADE)
#     data_update=models.DateTimeField(auto_now=True)
#     data_criacao=models.DateTimeField(auto_now=True)

