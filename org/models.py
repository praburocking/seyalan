from django.db import models
from django.contrib.auth import get_user_model
import uuid
from accounts.models import User,UserManager

# Create your models here.
class Org(models.Model):
        ORG_TYPE = (
        ('1', 'WORK_FLOW_MACHIN'),
    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    orgtype=models.TextField(max_length=1, choices=SHIRT_SIZES)
    members = models.ManyToManyField(User, through='OrgMembers')
    created_time=models.DateTimeField(auto_now_add=True)
    name=models.TextField(max_length=250)
    super_Admin=
    license=
    address=
    

class OrgMembers(models.Model):
      USER_TYPE = (
        ('1', 'SUPER_ADMIN'),
        ('2','ADMIN'),
        ('3','STD')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    created_time=
    modified_time=
    invited_time=
    
class Address(models.Model):
    org=models.OneTO