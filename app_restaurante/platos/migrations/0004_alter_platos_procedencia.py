# Generated by Django 4.1.7 on 2023-02-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0003_alter_platos_precio_alter_platos_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='sin procedencia', max_length=35),
        ),
    ]