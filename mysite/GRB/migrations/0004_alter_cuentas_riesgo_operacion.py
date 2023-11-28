# Generated by Django 3.2.8 on 2023-11-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0003_alter_cuentas_riesgo_operacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='riesgo_operacion',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='Riesgo por operación'),
        ),
    ]
