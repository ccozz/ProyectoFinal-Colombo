# Generated by Django 5.0 on 2023-12-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_pais_nombre_alter_cliente_pais_origen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pais',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pais_origen',
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincia',
            field=models.CharField(blank=True, choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], max_length=50),
        ),
    ]