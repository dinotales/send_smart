# Generated by Django 5.0.6 on 2024-07-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0009_imagem_delete_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='selecinar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='media/mensagem'),
        ),
    ]
