# Generated by Django 3.2.4 on 2021-07-30 19:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant_user_handle', '0002_auto_20210625_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StageKanbanMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='KanbanView',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('isDefault', models.BooleanField(default=False)),
                ('sequenceNumber', models.IntegerField()),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenant_user_handle.user')),
            ],
        ),
        migrations.CreateModel(
            name='KanbanUserPermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isActive', models.BooleanField(default=True)),
                ('kanbanView', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='kanbanview.kanbanview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanbanViews', to='tenant_user_handle.user')),
            ],
        ),
    ]
