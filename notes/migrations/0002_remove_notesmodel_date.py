# Generated by Django 5.0 on 2024-02-06 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesmodel',
            name='date',
        ),
    ]
