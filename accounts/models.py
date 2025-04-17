from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    aadhar = models.CharField(max_length=12, unique=True, null=True, blank=True)
    pan = models.CharField(max_length=10, unique=True, null=True, blank=True)