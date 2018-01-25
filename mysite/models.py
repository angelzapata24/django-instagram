from django.db import models
from django import forms


# Create your models here.
class Picture(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='mysite/static/mysite/images')

    def img_url(self):
        return self.photo.url[len('mysite/images/'):]


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    document = models.ForeignKey(
        Picture, on_delete=models.SET_NULL, blank=True, null=True)
