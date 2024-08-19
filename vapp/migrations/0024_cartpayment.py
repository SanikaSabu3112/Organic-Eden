# Generated by Django 5.0.6 on 2024-07-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0023_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdctdetails', models.CharField(blank=True, max_length=400, null=True)),
                ('priceitm', models.CharField(blank=True, max_length=400, null=True)),
                ('qty', models.CharField(blank=True, max_length=400, null=True)),
                ('qtyprice', models.CharField(blank=True, max_length=400, null=True)),
                ('farmer', models.CharField(blank=True, max_length=400, null=True)),
                ('fremail', models.CharField(blank=True, max_length=400, null=True)),
                ('totalprice', models.IntegerField(default=0)),
                ('order_id', models.CharField(max_length=100)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=0)),
            ],
        ),
    ]
