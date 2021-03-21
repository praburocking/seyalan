from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User

class create_form(UserCreationForm):
    class Meta(UserCreationForm):
        model=User
        fields=('email',)

class change_form(UserChangeForm):
    class Meta(UserChangeForm):
        model=User
        fields=('email',)
