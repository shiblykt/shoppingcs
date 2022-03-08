from django.db import models

# Create your models here.
class feature(models.Model):
    name= models.CharField(max_length=100)
    detaills: models.CharField(max_length=100)