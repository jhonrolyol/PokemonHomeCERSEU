# Generated by Django 4.1.7 on 2023-02-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0002_platos_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='sin generacion', max_length=35),
        ),
    ]
