# Generated by Django 3.2.8 on 2023-12-07 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GRB', '0006_trades_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trades',
            name='estado',
        ),
    ]
