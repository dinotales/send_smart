# Generated by Django 5.0.6 on 2024-07-26 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0005_delete_selecionados_alter_mensagem_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='texto',
        ),
    ]
