# Generated by Django 5.1.3 on 2024-11-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Piloto', '0011_remove_situacao_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='situacao',
            name='estaNaInstituicao',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Aluno vinculado na instituição?'),
        ),
    ]