# Generated by Django 2.0.2 on 2018-04-05 23:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180402_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format '123-456-7890'.", regex='^d{3}-d{3}-d{4}$')]),
        ),
    ]
