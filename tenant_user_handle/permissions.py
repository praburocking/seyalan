from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from accounts.models import OrgMembers



class TentantPermission(BasePermission):
    def has_permission(self, request, view):
        isAuthenticated=IsAuthenticated().has_permission(request,view)
        print("tenant permission check is authentication")
        if(isAuthenticated):
            print(type(request.tenant))
            print(type(request.user))
            orgMember=None
            try:
                orgMember=OrgMembers.objects.get(org=request.tenant,user=request.user)
            except (OrgMembers.DoesNotExist):
                return False;
            print(orgMember)
            if orgMember==None:
                return False
            else:
                return True
        else:
            return False

class IsNotAuthenticated(BasePermission):
    def has_permission(self,request,view):
        return not IsAuthenticated().has_permission(request,view)


