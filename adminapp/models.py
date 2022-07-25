from django.db import models

# Create your models here.

class MessageModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=225)

    class Meta:
        db_table= 'message'