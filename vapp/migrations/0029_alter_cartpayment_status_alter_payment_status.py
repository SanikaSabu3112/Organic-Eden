# Generated by Django 5.0.6 on 2024-08-10 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0028_payment_deliverystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartpayment',
            name='status',
            field=models.CharField(default='created', max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(default='created', max_length=20),
        ),
    ]
