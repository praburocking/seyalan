# Generated by Django 3.0.4 on 2021-06-05 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token_type', models.CharField(choices=[('U_V', 'USER_VERIFICATION'), ('P_R', 'PASSWORD_RECOVERY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expiration_in_minutes', models.PositiveIntegerField(blank=True, default=10080, null=True)),
                ('token', models.CharField(default=None, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('num_times_send', models.PositiveIntegerField(default=0)),
                ('extra_data', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('token_type', 'user')},
            },
        ),
    ]
