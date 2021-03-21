from django.urls import path,include
from .views import createUser,loginView,accountsView,userExist,accountsImageView,passwordChange,forgotPassword
from knox import views as knox_views
from userVerification import urls as mail_urls

urlpatterns=[
    path(r'signup',createUser.as_view()),
    path(r'login',loginView.as_view()),
    path(r'logout',knox_views.LogoutView.as_view()),
    path(r'accounts',accountsView.as_view()),
    path(r'signup/exist',userExist.as_view()),
    path(r'accounts/userimage',accountsImageView.as_view()),
    path(r'accounts/passwordchange',passwordChange.as_view()),
    path(r'logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path(r'forgotpassword',forgotPassword.as_view()),
    path('verify/', include(mail_urls)),
]
