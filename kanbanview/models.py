from typing import Sequence
from django.db import models
import uuid

# Create your models here.

class KanbanView(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(null=False,unique=True,max_length=250)
    isDefault=models.BooleanField(default=False)
    sequenceNumber=models.IntegerField(null=False)
    owner=models.OneToOneField("tenant_user_handle.User",on_delete=models.SET_NULL,null=True)
    

class KanbanUserPermission(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey("tenant_user_handle.User", on_delete=models.CASCADE,related_name='kanbanViews')
    kanbanView = models.ForeignKey(KanbanView, on_delete=models.CASCADE,related_name='users')
    isActive=models.BooleanField(default=True)

class Stage(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(null=False,max_length=250)
    

class StageKanbanMap(models.Model):
    pass