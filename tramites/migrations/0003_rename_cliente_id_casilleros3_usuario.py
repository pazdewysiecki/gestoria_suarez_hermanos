# Generated by Django 4.0.4 on 2022-05-27 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tramites', '0002_remove_casilleros3_vigencia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casilleros3',
            old_name='cliente_id',
            new_name='usuario',
        ),
    ]