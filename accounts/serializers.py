#from typing_extensions import Required
from .models import User,Org,OrgMembers,Domain
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from userVerification.Confirm import sendConfirm
from licenses.models import License
from userVerification.Confirm import sendConfirm
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.db import transaction
from sequences import get_last_value,get_next_value



# class ReporterSerializer(serializers.ModelSerializer):
#     id=serializers.UUIDField(read_only=True)
#     email = serializers.EmailField( required=True,validators=[UniqueValidator(queryset=User.objects.all())])
#     username = serializers.CharField(min_length=4)
#     class Meta:
#         model=User
#         fields=('id','username','email')
        
class MemberSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email=serializers.SerializerMethodField()
    class Meta:
        model=OrgMembers
        fields=['id','profile','created_time','modified_time','invited_time','org','user','username','email']
    def get_username(self,obj):
        return obj.user.username
    def get_email(self,obj):
        return obj.user.email

class UserSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    email = serializers.EmailField( required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=8,write_only=True)
    verified = serializers.CharField(read_only=True)
    created_time=serializers.DateTimeField(read_only=True)
    active=serializers.BooleanField(read_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'],username=validated_data['username'])
        sendConfirm(user,'U_V')
        print("$$$$$$$$$$$$$____$$$$$$$$$$")
        print(type(user))
        return user

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = User
        fields = ( 'id','username', 'email', 'password','verified','created_time','active')

class UserUpdateSerializer(serializers.ModelSerializer):
    username=serializers.CharField(min_length=4,required=False)
    email=serializers.EmailField(min_length=8,required=False,)
    class Meta:
        model=User
        fields=('username','email')

class OrgSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    orgtype=serializers.CharField(read_only=True)
    configured_members=MemberSerializer(many=True,required=False,read_only=True)
    created_time=serializers.DateTimeField(read_only=True)
    modified_time=serializers.DateTimeField(read_only=True)
    name=serializers.CharField(required=True)
    #domain=serializers.CharField(required=True,source='get_domain')
    domain = serializers.SerializerMethodField()
    #def get_domain

    def get_domain(self,obj):
            return Domain.objects.get(tenant=obj).domain
    class Meta:
        fields=['id','orgtype','created_time','modified_time','name','configured_members','domain','superAdmin']
        model=Org
    def create(self, validated_data):
         validated_data['schema_name']=str( get_next_value('schema_name',initial_value=1000))+"wm_db"
         print(validated_data)
         domain_name=validated_data.pop('get_domain')
         org=Org.objects.create(**validated_data)
         domain = Domain()
         domain.domain = domain_name+'.workmachine.com' # don't add your port or www here!
         domain.tenant = org
         domain.is_primary = True
         domain.save()
         OrgMembers.objects.create(org=org,user=org.superAdmin,profile=1)
         License.objects.create(org=org)
         return org
class OrgCreateSerializer(serializers.ModelSerializer):
    pass





class Signup_serializer(serializers.Serializer):
    user=UserSerializer()
    org=OrgSerializer()
    def create(self,validated_data):
           print(validated_data)
           user=UserSerializer(data=validated_data['user'])
           user.is_valid(raise_exception=True)
           user_model=user.save()

           org_data=validated_data['org'] 
           org_data['superAdmin']=user.data['id']  
           org_data['domain']=org_data['get_domain']
           org=OrgSerializer(data=validated_data['org'])
           print(validated_data['org'])
           org.is_valid(raise_exception=True)
           org_model=org.save()
           print("$$$$$$ check here")
           print(type(user))
           print(user.data)
           return {'user': user_model, 'org': org_model}




