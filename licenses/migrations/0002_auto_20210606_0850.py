# Generated by Django 3.0.4 on 2021-06-06 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='totalSpace',
        ),
        migrations.RemoveField(
            model_name='license',
            name='usedSpace',
        ),
    ]
