from django.db import models

# Create your models here.

class mensagem (models.Model):

    texto= models.CharField (max_length=500, blank=True, null=True)
