# Generated by Django 3.2.8 on 2023-11-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='fecha',
            field=models.DateTimeField(null=True, verbose_name='Fecha'),
        ),
    ]
