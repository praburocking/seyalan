# Generated by Django 3.0.4 on 2021-03-31 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_s3_storage.storage
import guardian.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('user_image', models.ImageField(blank=True, null=True, storage=django_s3_storage.storage.S3Storage(aws_s3_bucket_name='filesec-userimage'), upload_to='')),
                ('active', models.BooleanField(default=True)),
                ('other_info', models.TextField(null=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, guardian.mixins.GuardianUserMixin),
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('orgtype', models.TextField(choices=[('1', 'WORK_FLOW_MACHIN')], default='1', max_length=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrgMembers',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('profile', models.CharField(choices=[('1', 'ADMIN'), ('2', 'DATA_ADMIN'), ('3', 'STD')], max_length=5)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('invited_time', models.DateTimeField(null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Org')),
                ('reporting_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reporters', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='org',
            name='members',
            field=models.ManyToManyField(through='accounts.OrgMembers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='orgmembers',
            constraint=models.UniqueConstraint(fields=('user', 'org'), name='unique_user_per_org'),
        ),
    ]
