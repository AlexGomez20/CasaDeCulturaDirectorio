# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161020_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fechaNacimimiento',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fechaRegistro',
            field=models.DateField(verbose_name='Fecha de Registro'),
        ),
    ]