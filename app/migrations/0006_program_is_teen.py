# Generated by Django 2.0.2 on 2018-03-21 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180225_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='is_teen',
            field=models.BooleanField(default=False),
        ),
    ]
