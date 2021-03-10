# Generated by Django 3.1.5 on 2021-03-05 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0003_auto_20210305_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'permissions': (('is_jefe', 'Is Jefe'), ('is_coordinador', 'Is Coordinador'))},
        ),
        migrations.AlterModelOptions(
            name='jefe',
            options={'permissions': (('is_jefe', 'Is Jefe'),)},
        ),
        migrations.AlterModelOptions(
            name='ordentrabajo',
            options={'permissions': (('is_jefe', 'Is Jefe'), ('is_coordinador', 'Is Coordinador'))},
        ),
    ]