# Generated by Django 5.0.6 on 2024-07-08 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0015_cont_email_cont_name_cont_phonenumber'),
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
    ]
