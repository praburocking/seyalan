# Generated by Django 3.0.4 on 2021-06-06 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210606_0913'),
        ('licenses', '0002_auto_20210606_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='org',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Org'),
        ),
    ]
