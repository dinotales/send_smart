from django.db import models

# Create your models here.

class Csv(models.Model):
    arquivo= models.FileField (upload_to='csvs')
    data_upload= models.DateTimeField(auto_now_add=True)
    ativo= models.BooleanField(default=False)
    nome=models.CharField(max_length=200,unique=True)
    
    def __str__(self):
        return f"File id: {self.id}"
