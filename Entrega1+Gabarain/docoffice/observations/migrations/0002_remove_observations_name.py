# Generated by Django 4.1.4 on 2023-01-10 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observations',
            name='name',
        ),
    ]
