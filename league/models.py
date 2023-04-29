from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    Date_of_birth = models.DateField(null=True) 
    Gender = models.CharField( max_length=500,null=True)


class games( models.Model):
    Pitch = models.CharField(max_length=500)
    Address = models.TextField()