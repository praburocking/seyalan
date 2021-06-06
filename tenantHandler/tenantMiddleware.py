from tenant_schemas.middleware import BaseTenantMiddleware

class XHeaderTenantMiddleware(BaseTenantMiddleware):
    EXCLUDE_URLS=['/api/iam/login','/api/iam/org','/api/iam/accounts','/add']
    """
    Determines tenant by the value of the ``X-DTS-SCHEMA`` HTTP header.
    """
    def get_tenant(self, model, hostname, request):
        org_id = request.headers['org-id']
        return model.objects.get(id=org_id)
