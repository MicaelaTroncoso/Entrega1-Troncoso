# Generated by Django 4.1.2 on 2022-10-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil_cuit', models.CharField(max_length=40)),
                ('nombre_apellido', models.CharField(max_length=40)),
                ('domicilio', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=1)),
                ('nombre_apellido', models.CharField(max_length=40)),
                ('cuil_cuit', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('monto_sin_iva', models.DecimalField(decimal_places=2, max_digits=15)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
                ('precio_sin_iva', models.DecimalField(decimal_places=2, max_digits=15)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
