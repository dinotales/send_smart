# Generated by Django 5.0.6 on 2024-07-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_csv_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='nome',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
