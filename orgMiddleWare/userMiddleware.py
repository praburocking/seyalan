from rest_framework.request import Request
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import get_user
from knox.auth import TokenAuthentication

def get_token_user(request):
    user = get_user(request)
    if user.is_authenticated:
        return user
    try:
        user_auth = TokenAuthentication().authenticate(Request(request))
        if user_auth is not None:
            return user_auth[0]
    except:
        pass
    return user


class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("token authentication in middleware checking")
        if 'Authorization' in request.headers.keys():

            assert hasattr(request, 'session'), "The Django authentication middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
            request.user = SimpleLazyObject(lambda: get_token_user(request))

        response = self.get_response(request)
        return response