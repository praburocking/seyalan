from django.db import models

# Create your models here.


class Org(TenantMixin):
    ORG_TYPE = (
        ('1', 'WORK_FLOW_MACHIN'),
    )
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    accounts_org_id=models.UUIDField(null=False,blank=False)
    orgtype=models.TextField(max_length=1, choices=ORG_TYPE, default="1")
    created_time=models.DateTimeField(null=False,auto_now_add=True)
    modified_time=models.DateTimeField(null=False,auto_now=True)
    name=models.CharField(max_length=250)
    superAdmin=models.OneToOneField(User,on_delete=models.SET_NULL,related_name='+',null=True,blank=True,unique=True)

class User(models.Model):
    USER_STATUS=((1,'ACTIVE'),(2,'DELETED'),(3,'DEACTIVATED'))
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    accounts_user_id=models.UUIDField(null=False,blank=False)
    email=models.EmailField(unique=True,max_length=255)
    verified=models.BooleanField(null=False,default=False)
    username=models.CharField(null=False,max_length=255)
    created_time=models.DateTimeField(null=False,auto_now_add=True)
    modified_time=models.DateTimeField(null=False,auto_now=True)
    user_image=models.ImageField(null=True,storage=storage,blank=True)
    status=models.IntField(null=False,blank=False,choices=USER_STATUS)
    other_info=models.TextField(null=True)

