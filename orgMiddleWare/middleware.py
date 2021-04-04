from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from threading import local
from accounts.models import Org,OrgMembers
from sequences import get_range
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import status


USER_ATTR_NAME = getattr(settings, 'LOCAL_USER_ATTR_NAME', '_current_user')
ORG_ATTR_NAME = getattr(settings, 'LOCAL_ORG_ATTR_NAME', '_current_org')
RANGE_ATTR_NAME = getattr(settings, 'LOCAL_RANGE_ATTR_NAME', '_current_range')
EXCLUDE_URLS=['/api/iam/login','/api/iam/org','/api/iam/accounts']
_thread_locals = local()


def _do_set_current_user(user_fun):
    setattr(_thread_locals, USER_ATTR_NAME, user_fun.__get__(user_fun, local))

def _do_set_current_org(org_id):
    user=get_current_authenticated_user()
    if user is not None:
        cur_org=None
        try:
            cur_org=Org.objects.get(configured_members__user__id=user.id,id=org_id)
            print(cur_org)
        except Exception as e:
            print(org_id)
            print(user.id)
            print(e)
            return False
        
        if(cur_org==None):
            print(cur_org)
            return False
        else:
            setattr(_thread_locals, ORG_ATTR_NAME, cur_org)
            setattr(_thread_locals, RANGE_ATTR_NAME, get_range(cur_org.id))
            return True

def _set_current_user(user=None):
    '''
    Sets current user in local thread.

    Can be used as a hook e.g. for shell jobs (when request object is not
    available).
    '''
    _do_set_current_user(lambda self: user)



class ThreadLocalUserMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request.user closure; asserts laziness;
        # memorization is implemented in
        # request.user (non-data descriptor)
        if request.META['PATH_INFO'].startswith('/api'):
            _do_set_current_user(lambda self: getattr(request, 'user', None))
            org_set=True
            if( 'org-id' in request.headers.keys() and request.META['PATH_INFO'] not in EXCLUDE_URLS):
                org_set=_do_set_current_org( request.headers['org-id'])
            elif ('org-id' not in request.headers.keys() and request.META['PATH_INFO'] not in EXCLUDE_URLS):
                response= HttpResponse('{"details":"org header not found"}',status=status.HTTP_400_BAD_REQUEST)
                return response
            if not org_set:
                response= HttpResponse('{"details":"invalid org header"}',status=status.HTTP_400_BAD_REQUEST)
                return response
        response = self.get_response(request)
        return response


def get_current_user():
    current_user = getattr(_thread_locals, USER_ATTR_NAME, None)
    if callable(current_user):
        return current_user()
    return current_user

def get_current_org():
    current_org = getattr(_thread_locals, ORG_ATTR_NAME, None)
    if callable(current_org):
        return current_org()
    return current_org

def get_current_authenticated_user():
    current_user = get_current_user()
    if isinstance(current_user, AnonymousUser):
        return None
    return current_user


