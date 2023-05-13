from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    Date_of_birth = models.DateField(null=True) 
    Gender = models.CharField( max_length=500,null=True)


class games( models.Model):
    mer=(
        ('AM','AM'),
        ('PM','PM')
    )
    Pitch = models.CharField(max_length=500)
    Address = models.TextField()
    Date = models.DateField(null=True)
    Price = models.IntegerField(null=True)
    meridian = models.CharField(max_length=50,choices=mer,default='AM')
    Time = models.CharField( max_length=50,null=True)

