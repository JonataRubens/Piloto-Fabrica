# Generated by Django 5.1.3 on 2024-11-14 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Piloto', '0010_alter_situacao_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='situacao',
            name='name',
        ),
    ]