# Generated by Django 5.0.6 on 2024-07-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0003_alter_csv_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
