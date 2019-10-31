# Generated by Django 2.2.1 on 2019-10-31 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('CUIT', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('modelo', models.CharField(blank=True, max_length=30, null=True)),
                ('diagnostico', models.TextField()),
                ('presupuesto_detallado', models.TextField(null=True, verbose_name='Presupuesto detallado')),
                ('estado', models.CharField(choices=[('1', 'Ingresado'), ('2', 'Diagnosticando'), ('3', 'Esperando aprobacion'), ('4', 'Aprobado'), ('5', 'No aprobado'), ('6', 'Esperando repuestos'), ('7', 'Reparando'), ('8', 'Lista'), ('9', 'Entregada'), ('10', 'Entregada sin reparar')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SucursalOParticular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=30)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RepairApp.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(auto_now=True)),
                ('fecha_estimada', models.DateField(null=True)),
                ('descripcion_reparacion', models.TextField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RepairApp.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='sucursal_o_particular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RepairApp.SucursalOParticular', verbose_name='Sucursal o Particular'),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal_o_particular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RepairApp.SucursalOParticular')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion_trabajo', models.TextField(verbose_name='Descripción del trabajo')),
                ('reparacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RepairApp.Reparacion')),
            ],
        ),
    ]
