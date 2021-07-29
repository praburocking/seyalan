from typing import Sequence
from django.db import models
from accounts
import uuid

# Create your models here.

class KanbanView(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(null=False,unique=True)
    isDefault=models.BooleanField(default=False)
    sequenceNumber=models.IntegerField(null=False)
    owner=models.OneToOneField("tenant_user_handle.User",null=False)
    

class KanbanUserPermission(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey("tenant_user_handle.User", on_delete=models.CASCADE,related_name='kanbanViews')
    kanbanView = models.ForeignKey(KanbanView, on_delete=models.CASCADE,related_name='users')
    isActive=models.BooleanField(default=True)

class Stage(models.Model):
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    name=models.CharField(null=False)
    

class StageKanbanMap(models.Model):
    pass