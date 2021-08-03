# Generated by Django 3.2.5 on 2021-08-02 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('numero_orden', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Número orden')),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'OrdenDeTrabajo',
                'verbose_name_plural': 'OrdenDeTrabajos',
            },
        ),
        migrations.CreateModel(
            name='ImageOrdenTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_public', models.DateTimeField(auto_now_add=True, null=True)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarruselApp.ordentrabajo')),
            ],
            options={
                'verbose_name': 'ImagenOrdenDeTrabajo',
                'verbose_name_plural': 'ImagenOrdenDeTrabajos',
            },
        ),
    ]
