# Generated by Django 5.0.6 on 2024-06-20 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('bankname', models.CharField(max_length=30)),
                ('accountnumber', models.IntegerField()),
                ('ifsccode', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(default='farmer@gmail.com', max_length=254)),
                ('password', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('flicense', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField()),
                ('bankname', models.CharField(max_length=30)),
                ('accountnumber', models.IntegerField()),
                ('ifsccode', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(default='users@gmail.com', max_length=254)),
                ('password', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('frname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetFarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('farm', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vapp.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetUsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usr', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('tprice', models.IntegerField()),
                ('cartitm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.addproduct')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vapp.user')),
            ],
        ),
    ]
