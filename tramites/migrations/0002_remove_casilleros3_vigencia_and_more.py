# Generated by Django 4.0.4 on 2022-05-26 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tramites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casilleros3',
            name='vigencia',
        ),
        migrations.RemoveField(
            model_name='clientes_tramites',
            name='cliente_id',
        ),
        migrations.AddField(
            model_name='casilleros3',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='precio'),
        ),
        migrations.AddField(
            model_name='cedulas1',
            name='firma',
            field=models.CharField(blank=True, max_length=200, verbose_name='firma'),
        ),
        migrations.AddField(
            model_name='clientes_tramites',
            name='firma',
            field=models.CharField(blank=True, max_length=200, verbose_name='firma'),
        ),
        migrations.AddField(
            model_name='clientes_tramites',
            name='precio_tramite',
            field=models.IntegerField(null=True, verbose_name='precio_tramite'),
        ),
        migrations.AddField(
            model_name='clientes_tramites',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casilleros3',
            name='cliente_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casilleros3',
            name='vigencia_desde',
            field=models.DateField(blank=True, max_length=99, verbose_name='vigencia_desde'),
        ),
        migrations.AlterField(
            model_name='casilleros3',
            name='vigencia_hasta',
            field=models.DateField(blank=True, max_length=100, verbose_name='vigencia_hasta'),
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
