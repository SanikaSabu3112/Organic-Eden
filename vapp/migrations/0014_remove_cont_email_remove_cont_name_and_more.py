# Generated by Django 5.0.6 on 2024-07-08 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0013_rply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cont',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cont',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cont',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='cont',
            name='usrdetail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vapp.user'),
            preserve_default=False,
        ),
    ]
