from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return self.name 
    
    
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products')
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField() 
    rate = models.PositiveIntegerField(default=0)
    image_comment = models.ImageField(upload_to='commnts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
    
    