# Generated by Django 3.2.15 on 2022-09-09 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_resource_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='desc',
        ),
    ]
