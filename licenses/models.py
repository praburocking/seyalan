from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid
#from accounts.models import Org


# Create your models here.


LICENSE={
     "TRAIL": {"NAME": "TRAIL", "SIZE": 5000,"priceId":"Free","PRODUCT_ID":"Free","PRODUCT_ID":"Free"},
    "FREE": {"NAME": "Free", "SIZE": 500,"priceId":"Free","PRODUCT_ID":"Free","PRODUCT_ID":"Free"},
    "PAID1": {"NAME": "Paid1", "SIZE": 5000,"priceId":"price_1H3yk3AD7nX8Xg8myxZ505pY","PRODUCT_ID":""},
    "PAID2": {"NAME": "Paid2", "SIZE": 10000,"priceId":"price_1H3ynxAD7nX8Xg8mKDhsWjHT","PRODUCT_ID":""},
}


class License(models.Model):

    id=models.BigIntegerField(primary_key=True,editable=False)
    #org=models.OneToOneField(Org,related_name='License',on_delete=models.CASCADE)
    licenseType=models.CharField(max_length=10,default=LICENSE["TRAIL"]["NAME"])
    totalSpace=models.FloatField(default=LICENSE["FREE"]["SIZE"])
    usedSpace=models.FloatField(default=0)
