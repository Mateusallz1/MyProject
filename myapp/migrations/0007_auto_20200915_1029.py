# Generated by Django 3.1 on 2020-09-15 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200915_1028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person1',
            new_name='Person',
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 15, 10, 29, 9, 97772)),
        ),
    ]
