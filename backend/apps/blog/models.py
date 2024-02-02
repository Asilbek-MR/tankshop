from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Mainarticle (models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    creted = models.DateField()
    
    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    body = models.TextField()
    creted = models.DateField()
    
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    
    
    
class UserProfile(AbstractUser):
    summary = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    


class AddInformation(models.Model):
    high_resolution = models.CharField(
        max_length=3,
        choices=[
            ('yes', 'Yes'),
            ('no', 'No'),
        ],
        default='no', 
    )
    layered = models.CharField(
        max_length=3,
        choices=[
            ('yes', 'Yes'),
            ('no', 'No'),
        ],
        default='no', 
    )
    graphic_files_included = models.CharField(max_length=255)
    pixel_dimensions = models.CharField(max_length=50)
    print_dimensions = models.CharField(max_length=50)
    

class Quote(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    body = models.TextField()

class License(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()



class SocialMedia(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    link = models.URLField(max_length=255)
   