# Generated by Django 5.0.6 on 2024-07-04 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0010_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='buyitm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy', to='vapp.addproduct'),
        ),
    ]
