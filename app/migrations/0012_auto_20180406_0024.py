# Generated by Django 2.0.2 on 2018-04-06 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180405_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
