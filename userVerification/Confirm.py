from http import HTTPStatus
from rest_framework.decorators import api_view,authentication_classes,throttle_classes
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from datetime import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from hashlib import sha224
from random import randint, shuffle
from smtplib import SMTP
from threading import Thread
from django.core.mail import EmailMessage
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import get_resolver

from .errors import InvalidUserModel, EmailTemplateNotFound
from .errors import NotAllFieldCompiled
from rest_framework.authentication import BasicAuthentication




# Create your views here.
@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle,AnonRateThrottle])
@authentication_classes([BasicAuthentication])
def verify(request, email_token,token_type):
    try:
        #template = settings.EMAIL_PAGE_TEMPLATE
        #return render(request, template, {'success': verifyToken(email_token)})
        user=verifyToken(email_token,token_type)
        if user is not None:
            if token_type=='U_V':
                user.verified = True
                user.save()
                return HttpResponse('{"detail":"verified","message":"token verified"}', status=HTTPStatus.ACCEPTED,content_type='application/json')
            elif token_type=='P_R' and request.method == 'POST':
                if request.data['password'] is not None:
                    user.set_password(request.data['password'])
                    user.save()
                    return HttpResponse('{"detail":"password updated","message":"password updated try logging-in"}',status=HTTPStatus.OK,content_type='application/json')
                
        else:
            return HttpResponse('{"detail":"not verified","message":"token verified failed/invalid token"}',status=HTTPStatus.FORBIDDEN,content_type='application/json')
    except AttributeError:
        raise NotAllFieldCompiled('EMAIL_PAGE_TEMPLATE field not found')


def sendConfirm(user, token_type, **kwargs):
    from .models import Token
    try:
        email = user.email
        if token_type=='U_V':
            user.verified = False
            user.save()

        try:
            token = kwargs['token']
        except KeyError:
            alpha = [c for c in 'abcdefghijklmnopqrstuwxyz']
            shuffle(alpha)
            word = ''.join([a for a in alpha if randint(0, 1) == 1])
            token = str(sha224(bytes(email + str(dt.now()) + str(randint(1000, 9999)) + word, 'utf-8')).hexdigest())

        try:
            user_email=Token.objects.get(user=user,token_type=token_type)
            is_token_active=user_email.is_token_active()
            if is_token_active :
                token=user_email.token
            else:
                user_email.delete()
                user_email = Token.objects.create(user=user, token=token,token_type=token_type)
                user_email.save()
        except Token.DoesNotExist:
            user_email = Token.objects.create(user=user, token=token,token_type=token_type)
            user_email.save()
            pass

        #user_email = User.objects.create(user=user, email_token=token,token_type=token_type)
        
        t = Thread(target=sendConfirm_thread, args=(email, token,token_type))
        t.start()
    except AttributeError:
        raise InvalidUserModel('The user model you provided is invalid')


def sendConfirm_thread(email, token,token_type):
    try:
        sender = settings.EMAIL_SERVER
        link = settings.EMAIL_USER_VERIFICATION_LINK
        subject = settings.EMAIL_MAIL_SUBJECT
        address = settings.EMAIL_ADDRESS
        port = settings.EMAIL_PORT
        password = settings.EMAIL_PASSWORD
    except AttributeError:
        raise NotAllFieldCompiled('Compile all the fields in the settings')
    link=link+token_type+"/"+token
    try:
        html = settings.USER_VERIFICATION_HTML_TEMPLATE[token_type]
        html = render_to_string(html, {'link': link})
        msg = EmailMessage(subject, html,address, email.split(","))
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
    except AttributeError:
        pass

def verifyToken(email_token,token_type):
    from .models import Token
    try:
        user_email = Token.objects.get(token=email_token,token_type=token_type)
        if  user_email.is_token_active():
            user = get_user_model().objects.get(email=user_email.user.email)
            user_email.delete()
            return user
        else:
            return None
    except Token.DoesNotExist:
        return None

