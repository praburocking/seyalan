from .models import User,Org
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from userVerification.Confirm import sendConfirm



class reporterSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    email = serializers.EmailField( required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=4)
    class Meta:
        model=User
        fields=('id','username','email')

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
        return user

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = User
        fields = ( 'id','username', 'email', 'password','verified','created_time','active')

class UserUpdateSerializer(serializers.ModelSerializer):
    username=serializers.CharField(min_length=4,required=False)
    email=serializers.EmailField(min_length=8,required=False)
    class Meta:
        model=User
        fields=('username','email')

class OrgSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    orgtype=serializers.CharField(read_only=True)
    #members=reporterSerializer(many=True)
    created_time=serializers.DateTimeField(read_only=True)
    #name=serializers.CharField(min_length=5)
    modified_time=serializers.DateTimeField(read_only=True)
    
    class Meta:
        fields=['id','orgtype','created_time','modified_time','name']
        model=Org






