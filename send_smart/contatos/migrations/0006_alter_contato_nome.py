# Generated by Django 5.0.6 on 2024-07-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_alter_contato_contato_alter_contato_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
