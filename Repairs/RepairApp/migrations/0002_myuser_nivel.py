# Generated by Django 2.2.1 on 2019-11-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepairApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='nivel',
            field=models.CharField(choices=[('1', 'Técnico'), ('2', 'Dueño'), ('3', 'Empleado de Sucursal')], max_length=1, null=True),
        ),
    ]
