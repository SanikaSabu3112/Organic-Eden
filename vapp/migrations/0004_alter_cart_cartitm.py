# Generated by Django 5.0.6 on 2024-07-01 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0003_addproduct_crt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartitm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='vapp.addproduct'),
        ),
    ]
