# Generated by Django 2.0.2 on 2018-04-16 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_adult_confirmation_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adult',
            name='confirmation_number',
        ),
    ]