# Generated by Django 5.0.6 on 2024-07-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0022_payment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
