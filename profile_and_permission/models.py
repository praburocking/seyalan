from django.db import models
from tenant_user_handle.models import Org,User
import uuid
# Create your models here.

class Permission(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(max_length=250)
    sys_ref_name=models.CharField(max_length=250)
    desc=models.TextField(null=True)

class Profile(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(max_length=250)
    sys_ref_name=models.CharField(max_length=250)
    desc=models.TextField(null=True)
    users=models.ManyToManyField(User)
    permissions=models.ManyToManyField(Permission)









