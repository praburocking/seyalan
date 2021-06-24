from .models import User,Org
from accounts.models import User as accounts_User,Org as accounts_Org
from django_tenants.utils import schema_context
class tenant_user:
    def __init__(self,iam_org):
        self.iam_org=iam_org
    def create_tenant_user(self,acc_user):
        with schema_context(self.iam_org.schema_name):
            user=User(accounts_user_id=acc_user.id,email=acc_user.email,verified=acc_user.verified,username=acc_user.username,status=1,other_info=acc_user.other_info)
            user.save()
            return user
    def get_tenant_user_by_accounts_id(self,accounts_user_id):
        with schema_context(self.iam_org.schema_name):
            return User.objects.get(accounts_user_id=accounts_user_id)
    def get_tenant_user(self,id):
         with schema_context(self.iam_org.schema_name):
             return User.objects.get(id=id)
    def update_tenant_user(self,acc_user):
        with schema_context(self.iam_org.schema_name):
            user=User.objects.get(accounts_user_id=acc_user.id)
            if user is not None:
                user.email=acc_user.email
                user.verified=acc_user.verified
                user.user_image=acc_user.user_image
                user.other_info=acc_user.other_info
                user.update()
            return user

        
class tenant_org:
    def __init__(self,iam_org):
        self.iam_org=iam_org
    def create_tenant_org(self,acc_org):
        with schema_context(self.iam_org.schema_name):
            org=Org(accounts_org_id=acc_org.id,orgtype=acc_org.orgtype,name=acc_org.name,superAdmin=User.objects.get(accounts_user_id=acc_org.superAdmin.id))
            org.save()
            return org
    def get_tenant_org_accounts_id(self,accounts_org_id):
         with schema_context(self.iam_org.schema_name):
             return Org.objects.get(accounts_org_id=accounts_org_id)
    def get_tenant_org(self,id):
         with schema_context(self.iam_org.schema_name):
             return Org.objects.get(id=id)
    def update_tenant_org(self,acc_org):
        with schema_context(self.iam_org.schema_name):
            org=Org.objects.get(accounts_org_id=acc_org.id)
            org.orgtype=acc_org.orgtype
            org.name=acc_org.name
            org.superAdmin=User.objects.get(accounts_user_id=acc_org.superAdmin.id)
            org.update()
            return org

