from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import Org,Domain,OrgMembers,Domain,User
from django.db import transaction
from django.conf import settings

class Command(BaseCommand):
    help = 'Displays current time'
    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='emailID')
        parser.add_argument('org_name' ,type=str,help="org name")
    def handle(self, *args, **kwargs):
        email=kwargs['email']
        user=User.objects.get(email=email)
        orgName=kwargs['org_name']
        if not user.is_superuser:
            raise Exception('not a super user')
        domainName=settings.BASE_DOMAIN
        with transaction.atomic():
            org=Org(name=orgName,superAdmin=user,schema_name='public')
            org.save()
            domain=Domain()
            domain.domain = domainName # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = org
            domain.is_primary = True
            domain.save()
            orgMember=OrgMembers(user=user,org=org,profile=1,is_verified_member=True)
            orgMember.save()
            self.stdout.write(user.email)
            self.stdout.write(domainName)
            self.stdout.write(orgName)