from django.db import models
from django.contrib.auth.models import User

class ProductDetail(models.Model):

    option = (
        ("Men","Men"),
        ("Womans","Womens"),
        ("Kids","Kids")
    )
    ProductId = models.AutoField(primary_key=True)
    Product_Name=models.CharField(max_length=255)
    Product_Brand=models.CharField(max_length=255)
    Product_Discription=models.CharField(max_length=1000)
    Product_Price=models.IntegerField()
    Product_Category=models.CharField(max_length=255,choices=option)
    Product_Stock =models.PositiveIntegerField()
    Product_Image=models.ImageField(upload_to="product_image")
    Merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)




