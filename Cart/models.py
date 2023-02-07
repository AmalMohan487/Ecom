from django.db import models
from Product.models import ProductDetail
from django.contrib.auth.models import User

class Cart(models.Model):
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    numberofitems = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    status = models.BooleanField(default=False)
