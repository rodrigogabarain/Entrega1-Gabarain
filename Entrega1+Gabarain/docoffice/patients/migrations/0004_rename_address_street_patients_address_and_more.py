# Generated by Django 4.1.5 on 2023-01-10 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_patients_address_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='address_street',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patients',
            old_name='address_number',
            new_name='dni',
        ),
    ]
