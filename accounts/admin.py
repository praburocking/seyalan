from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User,Org,OrgMembers
from .forms import change_form,create_form
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    pass
    # add_form = create_form
    # form = change_form
    # model = User
    # list_display = ('email', 'staff', 'active',)
    # list_filter = ('email', 'staff', 'active',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Permissions', {'fields': ('staff', 'active')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'staff', 'active')}
    #     ),
    # )
    # search_fields = ('email',)
    # ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Org, CustomUserAdmin)
admin.site.register(OrgMembers, CustomUserAdmin)


