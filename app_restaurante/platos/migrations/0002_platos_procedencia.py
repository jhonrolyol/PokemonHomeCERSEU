# Generated by Django 4.1.7 on 2023-02-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='', max_length=50),
        ),
    ]
