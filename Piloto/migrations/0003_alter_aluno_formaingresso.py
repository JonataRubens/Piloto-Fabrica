# Generated by Django 5.1.3 on 2024-11-12 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Piloto', '0002_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='formaIngresso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Piloto.formaingresso', verbose_name='Forma de Ingresso'),
        ),
    ]