# Generated by Django 2.0.2 on 2018-04-05 23:47

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180405_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
