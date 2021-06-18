# Generated by Django 2.2.24 on 2021-06-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('DUI_ADMINISTRADOR', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CONTRASENA_ADMINISTRADOR', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('ID_BENEFICIARIO', models.AutoField(primary_key=True, serialize=False)),
                ('DUI_BENEFICIARIO', models.CharField(max_length=10)),
                ('NOMBRE_BENEFICIARIO', models.CharField(max_length=20)),
                ('APELLIDO_BENEFICIARIO', models.CharField(max_length=20)),
                ('DEPARTAMENTO_BENEFICIARIO', models.CharField(max_length=30)),
                ('MUNICIPIO_BENEFICIARIO', models.CharField(max_length=30)),
                ('DIRECCION_BENEFICIARIO', models.CharField(max_length=100)),
                ('RECEPTOR_BENEFICIARIO', models.BooleanField(choices=[(True, 'Si'), (False, 'No')])),
                ('ENTIDAD_BENEFICIARIO', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('ID_DEPARTAMENTO', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('NOMBRE_DEPARTAMENTO', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('ID_ENTIDAD', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE_ENTIDAD', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('ID_MUNICIPIO', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('NOMBRE_MUNICIPIO', models.CharField(max_length=30)),
                ('ID_DEPARTAMENTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('ID_PAQUETE', models.AutoField(primary_key=True, serialize=False)),
                ('CANTIDAD', models.IntegerField()),
                ('ID_BENEFICIARIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.Beneficiario')),
                ('ID_DEPARTAMENTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.Departamento')),
                ('ID_ENTIDAD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.Entidad')),
                ('ID_MUNICIPIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Principal.Municipio')),
            ],
        ),
    ]