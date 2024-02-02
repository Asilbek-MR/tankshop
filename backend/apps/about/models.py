from django.db import models

# Create your models here.


class About(models.Model):
    titile = models.CharField(max_length=255)
    body = models.TextField()
    images = models.ImageField(upload_to='about/images')




class Brands(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands/images')
    
    
    
class Honors(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    


class Aboutme(models.Model):
    name = models.CharField(map_length=255)
    image = models.ImageField(upload_to='about/images', blank=True)
    # author = models.ForeignKey()
    body = models.TextField()
    
    
    
    
    

















