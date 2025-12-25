from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pic/', default='profile_pic/default.png')
    address = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.username
    