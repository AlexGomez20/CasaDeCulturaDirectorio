# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161020_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('fechaRealizacion', models.DateField(verbose_name='fecha realizacion')),
                ('hora', models.TimeField()),
                ('descripcion', models.TextField(max_length=800)),
                ('imagen', models.CharField(max_length=100)),
                ('fechaPublicacion', models.DateField(verbose_name='fecha publicacion')),
                ('puntuacion', models.IntegerField(default=0)),
                ('visitas', models.IntegerField(default=0)),
                ('autorizado', models.BinaryField(default=0)),
            ],
            options={
                'ordering': ['fechaRealizacion'],
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['-fechaRegistro'], 'verbose_name': 'pefil', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AddField(
            model_name='perfil',
            name='autorizado',
            field=models.BinaryField(default=0),
        ),
        migrations.AddField(
            model_name='perfil',
            name='fechaNacimiento',
            field=models.DateField(auto_now=True, verbose_name='fecha nacimiento'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='fechaRegistro',
            field=models.DateField(auto_now=True, verbose_name='fecha registro'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='sexo',
            field=models.BinaryField(default=0),
        ),
    ]