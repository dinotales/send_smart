# Generated by Django 5.0.6 on 2024-07-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='nome',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
