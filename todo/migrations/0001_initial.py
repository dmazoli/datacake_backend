# Generated by Django 3.2.9 on 2021-12-02 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Tarefa')),
                ('inicio', models.DateField(default=datetime.datetime.now, verbose_name='Data de início')),
                ('fim', models.DateField(default=datetime.datetime.now, verbose_name='Data final')),
                ('status', models.BooleanField(verbose_name='Finalizado?')),
            ],
            options={
                'ordering': ['-inicio'],
            },
        ),
    ]
