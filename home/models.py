from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=130)
    email=models.CharField(max_length=150)
    message=models.TextField()
    # message=models.CharField(max_length=130)
