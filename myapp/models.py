from distutils.command.upload import upload
from django.db import models

# Create your models here.
class gallery(models.Model):
    img = models.ImageField(upload_to='pics')