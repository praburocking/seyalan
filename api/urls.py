# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('iam/',include('accounts.urls')),
    path('verify/',include('userVerification.urls'))
]
