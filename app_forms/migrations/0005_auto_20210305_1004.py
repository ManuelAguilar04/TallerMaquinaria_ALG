# Generated by Django 3.1.5 on 2021-03-05 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0004_auto_20210305_0913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reparacion',
            options={'permissions': (('is_jefe', 'Is Jefe'), ('is_coordinador', 'Is Coordinador'), ('is_empleado', 'Is Empleado'))},
        ),
    ]
