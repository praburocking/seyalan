# Generated by Django 3.0.4 on 2021-06-06 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210606_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='superAdmin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
