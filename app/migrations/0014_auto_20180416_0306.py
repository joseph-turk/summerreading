# Generated by Django 2.0.2 on 2018-04-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20180416_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
