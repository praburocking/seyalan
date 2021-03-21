from .Confirm import verify
from django.urls import path

urlpatterns = [
    path('<str:token_type>/<str:email_token>', verify)
]
