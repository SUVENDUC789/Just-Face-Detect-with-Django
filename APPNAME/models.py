from django.db import models

# Create your models here.

class Image(models.Model):
    title=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='myimage')
