# Generated by Django 2.0.2 on 2018-04-16 03:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180406_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adult',
            name='notify',
        ),
        migrations.AlterField(
            model_name='adult',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]