# Generated by Django 5.0.6 on 2024-08-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0010_imagem_selecinar_alter_imagem_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='mensagem/'),
        ),
    ]
