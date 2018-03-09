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



class Comment(models.Model):
    post = models.ForeignKey('gram.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=50,null=False, blank=False)

    class Meta:
        ordering =['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save


    @classmethod
    def search_by_username(cls,search_term):
        username = cls.objects.filter(username__icontains=search_term)
        return username



class Post(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=60, null=True)
    caption = HTMLField(null=True)
    likes = models.IntegerField(null =True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.ForeignKey(Profile, null=True)
