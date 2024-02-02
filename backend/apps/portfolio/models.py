from django.db import models
from apps.blog.models import UserProfile
from apps.about.models import About
from apps.shop.models import Product
# Create your models here.

class MainCategory(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=25)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.title}'
    
    
    

class Supplier(models.Model):
    title = models.CharField(max_length=250)
    clients = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    role = models.ManyToManyField(Branding, blank=True)
    website = models.URLField(max_length=255)
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    body = models.TextField()
    images = models.ImageField(upload_to='project/images', blank=True)
    projectimage = models.ImageField(upload_to='project/', blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = models.TextField()
    
    
    def __str__(self):
        return f'{self.title}'
    
    
    
    