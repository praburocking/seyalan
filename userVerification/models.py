from django.contrib.auth import get_user_model
from django.db import models
import uuid
from datetime import timedelta
from django.utils import timezone

class Token(models.Model):
    class Meta:
         unique_together = (('token_type', 'user'),)
    TOKEN_TYPE = (('U_V', 'USER_VERIFICATION'),('P_R','PASSWORD_RECOVERY'))
    id=models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token_type=models.CharField(max_length=10, choices=TOKEN_TYPE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    expiration_in_minutes = models.PositiveIntegerField(null=True, blank=True, default=60*24*7)
    token = models.CharField(max_length=100, null=True, default=None)
    is_active=models.BooleanField(default=True)
    num_times_send=models.PositiveIntegerField(default=0)
    extra_data = models.TextField(null=True, blank=True)

    def is_token_active(self):
         return (self.is_active  and self.token and (self.expiration_in_minutes is None or timezone.now() <= self.created_at + timedelta(minutes=self.expiration_in_minutes)))

    def get_type(self):
         return self.token_type; 
