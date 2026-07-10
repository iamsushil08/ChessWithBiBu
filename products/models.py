from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from cloudinary.models import CloudinaryField
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    
    def _str_(self):
        return self.name
        
class Contact(models.Model):
    first_name=models.CharField(max_length=100);
    last_name=models.CharField(max_length=100);
    email=models.EmailField();
    message=models.TextField();
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.last_name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  
    
    class Meta:
        ordering = ['-created_at']  