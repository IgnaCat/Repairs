# Generated by Django 2.2.1 on 2019-11-05 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RepairApp', '0003_myuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='admin',
        ),
    ]
