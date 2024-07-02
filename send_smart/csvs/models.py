from django.db import models

# Create your models here.

class Csv(models.Model):
    arquivo= models.FileField (upload_to='csvs')
    data_upload= models.DateTimeField(auto_now_add=True)
    ativo= models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
