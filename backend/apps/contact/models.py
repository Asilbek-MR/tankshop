from django.db import models
from apps.blog.models import UserProfile

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    
    

