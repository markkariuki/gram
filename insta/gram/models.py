from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Post(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30, null=True)
    image_caption = models.TextField(null =True)
    likes = models.IntegerField(null =True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)
    comments = models.TextField(null=True)


class Comments(models.Model):
    name = models.CharField(max_length =30)
    author = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
