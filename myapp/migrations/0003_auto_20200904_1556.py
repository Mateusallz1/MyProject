# Generated by Django 3.1 on 2020-09-04 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200904_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='shirt_size',
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='myapp.manufacter')),
            ],
        ),
    ]
