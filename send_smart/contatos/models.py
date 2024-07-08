from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contato(models.Model):
    nome= models.CharField(max_length=100, unique=True)
    contato=models.CharField(max_length=20)
    # gestor= models.ForeignKey(User, on_delete=models.CASCADE)
    data_update=models.DateTimeField(auto_now=True)
    data_criacao=models.DateTimeField(auto_now=True)
    enviar=models.BooleanField(default=False)


    def __str__ (self):
        return f"{self.nome}-{self.contato}"
    