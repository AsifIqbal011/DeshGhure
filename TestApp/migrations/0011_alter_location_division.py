# Generated by Django 5.2 on 2025-04-19 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0010_division_alter_location_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TestApp.division'),
        ),
    ]
