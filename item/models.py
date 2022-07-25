from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=10)
    product_details = models.TextField(max_length=225)
    product_image = models.FileField(upload_to="static/image/item",blank=False)
    product_description = models.TextField(max_length=225,default="No Description Avilable")

    class Meta:
        db_table= 'item'


class BuyProductModel(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,default='delivered')

    class Meta:
        db_table= 'buy'



