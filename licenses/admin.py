from django.contrib import admin
from .models import License
# Register your models here.
class LicenseAdmin(admin.ModelAdmin):
    pass
admin.site.register(License, LicenseAdmin)