# Generated by Django 5.0.4 on 2024-04-20 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0003_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='habitaciones.categoria'),
        ),
    ]
