# Generated by Django 5.0.6 on 2024-07-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contato_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='contato',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]