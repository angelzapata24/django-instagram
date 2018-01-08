from django.db import models
from django import forms


# Create your models here.
class Picture(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='mysite/static/mysite/images')
