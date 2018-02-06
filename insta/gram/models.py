from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.



class Post(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=60, null=True)
    caption = HTMLField(null=True)
    likes = models.IntegerField(null =True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)



class Comments(models.Model):
    name = models.CharField(max_length =30)
    author = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
