from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,UserUpdateSerializer,OrgSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .models import User,Org,OrgMembers
from django.http.response import HttpResponse
from django.core.files import File
from .email import user_mail
# from licenses.models import License,LICENSE
# from licenses.serializer import LicenseSerializer
# from licenses.util import LicenseUtil
from django.contrib.auth import get_user_model
#from payments.payment_util import create_customer,get_customer
from http import HTTPStatus
from userVerification.Confirm import sendConfirm
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
import logging
logger = logging.getLogger(__name__)  # eg: log_viewer_demo/log_viewer_demo/logger.py
#f_handler=logging.FileHandler('logs/app.log')
#logger.addHandler(f_handler)
logger.setLevel(logging.INFO)

# Create your views here.
class CurrentOrgView(APIView):
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      def get(self,request,id):
        if(request.user.is_authenticated):
            queryset=Org.objects.filter(configured_members__user__id=request.user.id,id=id)
            serializer=OrgSerializer(queryset,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data={"details":"invalid data"})



class OrgView(APIView):
      permission_classes = [IsAuthenticated]
      authentication_classes = [TokenAuthentication]
      def get(self,request):
        if(request.user.is_authenticated):
            queryset=Org.objects.filter(configured_members__user__id=request.user.id)
            serializer=OrgSerializer(queryset,many=True)
            return Response(data=serializer.data)
        else:
            return Response(data={"details":"invalid data"})



      def post(self,request,format='json'):
        if request.user.is_authenticated:
            data=request.data
            created_Org=Org.objects.create(name=request.data["name"])
            OrgMembers.objects.create(org=created_Org,user=request.user,profile=1)
            org_serializer=OrgSerializer(Org)
            if org_serializer:
                 org=org_serializer.save()
                 if org:
                    return Response(data=org_serializer.data,status=status.HTTP_201_CREATED)
                 else:
                    return Response(data={"detail": "exception in creating the org kindly try again latter"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"detail": "no user found"}, status=status.HTTP_400_BAD_REQUEST)
          
    




class createUser(APIView):

    authentication_classes = [BasicAuthentication]
    throttle_scope = 'signin/signup'
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # licen= License.objects.create(userId=user,licenseType=LICENSE["FREE"]["NAME"],totalSpace=LICENSE["FREE"]["SIZE"])
            # licenSerializer=LicenseSerializer(licen)
            # stripe_customer=create_customer(user=user,license=licen)
            # print(stripe_customer)
            # logger.info("license serialiser data ==> %s",licenSerializer.data)
            # logger.info("type of the data %s",type(licenSerializer.data))
            newLicenseData={}
             #{"stripe_customer_id":stripe_customer.stripe_customer_id}#licenSerializer.data["stripe_customer_id=stripe_customer.stripe_customer_id
            # newLicenseData.update(licenSerializer.data)
            if user:
                #ue=user_mail(user.email)
                #ue.welcome_email(user.username)
                return Response({"user": serializer.data, "authtoken": AuthToken.objects.create(user)[1], "license": newLicenseData},
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class userExist(APIView):
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        email = None
        username = None
        user = None
        if "email" in request.query_params.keys():
            email = request.query_params['email']
            user = get_object_or_404(User.objects.all(), email=email)
            return (Response(status=status.HTTP_200_OK, data={"detail": "found"}))
        elif "username" in request.query_params.keys():
            username = request.query_params["username"]
            user = get_object_or_404(User.objects.all(), username=username)
            return (Response(status=status.HTTP_200_OK, data={"detail": "found"}))
        else:
            return Response(data={"details": "invalid param"}, status=status.HTTP_400_BAD_REQUEST)



class loginView(APIView):
    authentication_classes = [BasicAuthentication]
    throttle_scope = 'signin/signup'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            if not request.user.is_authenticated:
                user = authenticate(username=request.data['email'], password=request.data['password'])
                print(user)
                if user is not None : #and user.verified:
                    license_value=None
                    # login(request,user)
                    # licenseUtil=LicenseUtil(userId=user.id)
                    # license_value=licenseUtil.getLicenseJo()
             
                    # license_value["stripe_customer_id"]=get_customer(user=user).stripe_customer_id
                    # print(license_value)
                    return Response(data={"user": UserSerializer(instance=user).data, "authtoken": AuthToken.objects.create(user)[1], "license": license_value})
                elif user is not None and not user.verified:
                    sendConfirm(user,'U_V')
                    return Response(data={"detail": "user not verified, new email send please verify the user"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response(data={"detail": "invalid email/password"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(data={"detail": request.user.username + " already logged in"},
                                status=status.HTTP_401_UNAUTHORIZED)

        except KeyError:
            return Response(data={"detail": "invalid inputdata"}, status=status.HTTP_400_BAD_REQUEST)


class accountsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def delete(self, request, format='json'):
        if request.user.is_authenticated:
            queryset = User.objects.all()
            queryset = get_object_or_404(queryset, pk=request.user.id)
            queryset.delete()
            return Response(data={"detail": "user deleted"}, status=status.HTTP_200_OK)

    def get(self, request):
        if request.user.is_authenticated:
            queryset = User.objects.all()
            user = get_object_or_404(queryset, pk=request.user.id)
            US = UserSerializer(user)
            license_value=None
            # licenseUtil = LicenseUtil(userId=user)
            # license_value=licenseUtil.getLicenseJo()
            # license_value["stripe_customer_id"]=get_customer(user=user).stripe_customer_id
            return Response(data={"user":US.data,"license":license_value})
        else:
            return Response(data={"detail": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            queryset=User.objects.all()
            queryset=get_object_or_404(queryset,pk=request.user.id)
            user_serializer=UserUpdateSerializer(queryset,data=request.data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response(data=user_serializer.data)




class accountsImageView(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            queryset = User.objects.all()
            queryset = get_object_or_404(queryset, pk=request.user.id)
            if not queryset.user_image == None:
                userimage = queryset.user_image
                response=HttpResponse(content=userimage, content_type='image/*')
                response['Content-Disposition'] = 'attachment; filename="'+userimage.name+'"'
                response['X-Frame-Options']='SAMEORIGIN'
                return response
            else:
                return Response(data={"detail": "no image"})
        else:
            return Response({"detail": "not authenticated"})

    def post(self, request):
        if (request.user.is_authenticated and 'file' in request.data.keys()):
            queryset = User.objects.all()
            queryset = get_object_or_404(queryset, pk=request.user.id)
            queryset.user_image = File(request.data['file'])
            queryset.user_image.name = str(queryset.id) + '.' + queryset.user_image.name.split('.')[1]
            queryset.save()
            print(queryset.user_image)
            return Response(data={"detail": "image added"})
        else:
            return Response({"detail": "not authenticated"})

class passwordChange(APIView):
    throttle_scope = 'reset'
    def post(self,request):
        if(request.user.is_authenticated):
            if authenticate(username=request.user.email, password=request.data['old_password']) is not None:
                user=request.user
                user.set_password(request.data['new_password'])
                user.save()
                return Response(data={"detail":"password updated"},status=HTTPStatus.OK)
            else:
                return Response(data={"detail":"old_password is incorrect"},status=HTTPStatus.FORBIDDEN)
        else:
            return Response(data={"detail":"not authenticated"},status=HTTPStatus.FORBIDDEN)    

class forgotPassword(APIView):
    throttle_scope = 'reset'
    def post(self,request):
        if(request.user.is_authenticated):
            return Response(data={"detail":"user already signed in"},status=HTTPStatus.BAD_REQUEST)
        else:
            queryset = User.objects.all()
            user = get_object_or_404(queryset, email=request.data["email"])
            sendConfirm(user,'P_R')
            return Response(data={"details":"recovery mail is sent to the registered mail"},status=HTTPStatus.ACCEPTED)

# class orgView(APIView):
#     def get(self,request):
#         if(request.user.is_authenticated):
#             queryset=Org.objects.all()
#             serializer=OrgSerializer(queryset,many=True)
#             return Response(data=serializer.data)
#         else:
#             return Response(data={"details":"invalid data"})

            