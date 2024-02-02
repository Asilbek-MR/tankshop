from django.db import models
from apps.blog.models import Category, SocialMedia, AddInformation, License,Comment,UserProfile
# Create your models here.

class ProjectVisual(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='/project/visual')
    
    def __str__(self):
        return f'{self.title}'
    
    
class Tag(models.Model):
    title = models.CharField(max_length=25)
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.title}'
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    socialmedia = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    desciption = models.TextField(blank=True)
    addinformation = models.ForeignKey(AddInformation, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    reviews = models.ForeignKey(Comment, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.title}'
    


class ShoppingCart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    stokstatus = models.CharField(
        max_length=3,
        choices=[
            ('In stock', 'Yes'),
            ('No stock', 'No'),
        ],
        default='no', 
    )
    def __str__(self):
        return f'{self.user}'




class BillingDetail(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.IntegerField(max_length=10)
    ordernote = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    
class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subtotal = models.IntegerField()
    ordertotal = models.IntegerField()
    billing = models.ForeignKey(BillingDetail, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'


class Wishlist(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'