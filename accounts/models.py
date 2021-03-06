from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django_s3_storage.storage import S3Storage
import uuid
import guardian
from guardian.mixins import GuardianUserMixin
from django.contrib.auth.models import PermissionsMixin
from sequences import get_last_value,get_next_value,create_org_space,get_space
storage = S3Storage(aws_s3_bucket_name='filesec-userimage')
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from licenses.models import License
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,username,**kargs):
        if not email:
            raise ValueError('Email field needed')
        if not password:
            raise ValueError('Password field is needed')
        if not username:
            username=email.split('@')[0]
        
        user = self.model(email=self.normalize_email(email),username=username,**kargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password,**kargs):
        user = self.create_user(email, password=password,**kargs)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,**kargs):
        user = self.create_user(email=email,password=password,**kargs)
        user.staff = True
        user.admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin,guardian.mixins.GuardianUserMixin):

    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    email=models.EmailField(unique=True,max_length=255)
    verified=models.BooleanField(null=False,default=False)
    username=models.CharField(null=False,max_length=255)
    created_time=models.DateTimeField(null=False,auto_now_add=True)
    modified_time=models.DateTimeField(null=False,auto_now=True)
    user_image=models.ImageField(null=True,storage=storage,blank=True)
    active = models.BooleanField(default=True)
    other_info=models.TextField(null=True)


    #admin properties
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    is_superuser=models.BooleanField(default=False)


    # def save(self,*args,**kwargs):
    #     if self.id is None:
    #         user_id=get_next_value('_user_id_',initial_value=111111111)
    #         self.id=user_id
    #     super(User,self).save(*args,**kwargs)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS = ['username']

    def is_verified(self):
        return self.verified

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

        
    @property
    def is_staff(self):

        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()




class Org(TenantMixin):
    ORG_TYPE = (
        ('1', 'WORK_FLOW_MACHIN'),
    )
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    orgtype=models.TextField(max_length=1, choices=ORG_TYPE, default="1")
    members = models.ManyToManyField(User, through='OrgMembers',through_fields=('org', 'user'))
    created_time=models.DateTimeField(null=False,auto_now_add=True)
    modified_time=models.DateTimeField(null=False,auto_now=True)
    name=models.CharField(max_length=250)
    superAdmin=models.OneToOneField(User,on_delete=models.SET_NULL,related_name='+',null=True,blank=True,unique=True)

        
    def __str__ (self):
        return self.name
    def get_domain(self):
        return Domain.objects.get(tenant=self).domain

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         self.id=create_org_space()
    #     super(Org, self).save(*args, **kwargs)

        
        


class OrgMembers(models.Model):
    PROFILE = (
        ('1', 'ADMIN'),
        ('2','DATA_ADMIN'),
        ('3','STD')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='configured_orgs')
    org = models.ForeignKey(Org, on_delete=models.CASCADE,related_name='configured_members')
    id=models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    profile=models.CharField(max_length=5,choices=PROFILE)
    created_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField(auto_now=True)
    invited_time=models.DateTimeField(null=True,blank=True)
    reporting_to=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,related_name="reporters",null=True)
    is_verified_member=models.BooleanField(default=False)
    class Meta:
        constraints = [
                    UniqueConstraint(fields=['user','org'], name='unique_user_per_org')           
        ]
    # def save(self,*args,**kwargs):
    #     if self.id is None:
    #         print(self.org.id)
    #         cur_range=get_space(self.org.id)

    #         print(cur_range)
    #         str_init=str(cur_range)+"000000000000"
    #         self.id=get_next_value(self.org.id, initial_value=int(str_init))
    #     super(OrgMembers,self).save(*args,**kwargs)

class Domain(DomainMixin):
        pass