# Generated by Django 3.1 on 2020-09-18 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200918_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacter',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Person_1',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='coberturas',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Cobertura',
        ),
        migrations.DeleteModel(
            name='CPF',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Manufacter',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='PessoaFisica',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]