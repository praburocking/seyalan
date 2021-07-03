from knox.auth import TokenAuthentication


class tenentAuth(TokenAuthentication):
     def authenticate(self, request):
         user,auth_token=super(self).authenticate(request)
         request.tenant

