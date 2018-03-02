from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)



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

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering =['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save
