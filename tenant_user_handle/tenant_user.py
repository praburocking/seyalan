from .models import User,Org
from accounts.models import User as accounts_User,Org as accounts_Org
class tenant_user:
    def create_tenant_user(acc_user):
        user=User(accounts_org_id=acc_user.id,email=acc_user.email,verified=acc_user.verified,username=acc_user.username,user_image=acc_user.user_image,status=1,other_info=acc_user.other_info)
        user.save()
        return user
    def get_tenant_user_by_accounts_id(accounts_user_id):
       return User.objects.get(accounts_user_id=accounts_user_id)
    def get_tenant_user(id):
        return User.objects.get(id=id)
    def update_tenant_user(acc_user):
        user=User.objects.get(accounts_user_id=acc_user.id)
        if user is not None:
            user.email=acc_user.email
            user.verified=acc_user.verified
            user.user_image=acc_user.user_image
            user.other_info=acc_user.other_info
            user.update()
        return user

        
class tenant_org:
    def create_org(acc_org):
        org=Org(accounts_org_id=acc_org.id,orgtype=acc_org.orgtype,name=acc_org.name,superAdmin=User.objects.get(accounts_user_id=acc_org.superAdmin.id))
        org.save()
        return org
    def get_tenant_org_accounts_id(accounts_org_id):
        return Org.objects.get(accounts_org_id=accounts_org_id)
    def get_tenant_org(id):
        return Org.objects.get(id=id)
    def update_tenant_org(acc_org):
        org=Org.objects.get(accounts_org_id=acc_org.id)
        org.orgtype=acc_org.orgtype
        org.name=acc_org.name
        org.superAdmin=User.objects.get(accounts_user_id=acc_org.superAdmin.id)
        org.update()
        return org

