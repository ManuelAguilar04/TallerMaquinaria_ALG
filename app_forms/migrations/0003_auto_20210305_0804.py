# Generated by Django 3.1.5 on 2021-03-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0002_auto_20210303_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'permissions': (('jefe', 'jefe'),)},
        ),
        migrations.AlterModelOptions(
            name='equipo',
            options={'permissions': (('is_jefe', 'Is Jefe'), ('is_coordinador', 'Is Coordinador'))},
        ),
        migrations.AlterModelOptions(
            name='jefe',
            options={'permissions': (('jefe', 'jefe'),)},
        ),
        migrations.AlterModelOptions(
            name='ordentrabajo',
            options={'permissions': (('jefe', 'jefe'),)},
        ),
        migrations.AlterField(
            model_name='ordentrabajo',
            name='codOrdenTrab',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Código de orden'),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='descripActi',
            field=models.CharField(max_length=50, null=True, verbose_name='Descripción de la actividad'),
        ),
    ]
