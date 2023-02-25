# Generated by Django 4.1.7 on 2023-02-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(default='', max_length=27)),
                ('dni', models.CharField(default='00000000', max_length=8)),
                ('vigente', models.BooleanField(default=True)),
            ],
        ),
    ]