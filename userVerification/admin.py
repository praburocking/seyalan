from django.contrib import admin
from django.conf import settings

from .models import Token


admin.site.register(Token)

