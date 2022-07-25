from django.db import models
from item.models import ProductModel
from django.contrib.auth.models import User

# Create your models here.


class UserCartModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user_if = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    class Meta:
        db_table= 'cart'

