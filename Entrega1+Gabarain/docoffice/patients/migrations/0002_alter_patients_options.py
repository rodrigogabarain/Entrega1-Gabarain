# Generated by Django 4.1.5 on 2023-01-08 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patients',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]