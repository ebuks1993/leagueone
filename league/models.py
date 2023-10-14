from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 

# Create your models here.



class CustomUserManager(UserManager):
    def get_by_natural_key(self, email):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: email})


class User(AbstractUser):
    email=models.EmailField(unique=True)
    Date_of_birth = models.DateField(null=True) 
    Gender = models.CharField( max_length=500,null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()

    def save(self,*args,**kwargs):
        self.email=str(self.email).lower()
        super(User,self).save(*args,**kwargs)


class Pitch(models.Model):
    Name = models.CharField( max_length=1500)
    Address = models.TextField()
    Price = models.IntegerField()
    players = models.IntegerField()
    pitchmap = models.URLField( max_length=2000,null=True)


    def __str__(self):
        return self.Name

class Sport(models.Model):
    name = models.CharField( max_length=1500)

    def __str__(self):
        return self.name
    
class Agerange(models.Model):
    AgeGrade = models.CharField( max_length=1500)

    def __str__(self):
        return self.AgeGrade

class Games( models.Model):
    mer=(
        ('AM','AM'),
        ('PM','PM')
    )
    sta=(
        ('INCOMPLETE','INCOMPLETE'),
        ('COMPLETE','COMPLETE')
    )
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    Agerange = models.ForeignKey(Agerange, on_delete=models.CASCADE,null=True)
    Date = models.DateField(null=True)
    meridian = models.CharField(max_length=50,choices=mer,default='AM')
    Time = models.CharField( max_length=50,null=True)
    spot = models.IntegerField(default=0)
    Status = models.CharField( max_length=50, choices=sta,default='INCOMPLETE')
    # mins = models.IntegerField()

    def __str__(self):
        return f'{self.pitch} --{self.Date}--{self.Time} '

class GameSelect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    Amount = models.IntegerField( null=True)
    createdat = models.DateField(auto_now_add=True , null=True)

class trans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(GameSelect, on_delete=models.DO_NOTHING)
    inflow = models.IntegerField(default=0)  
    outflow = models.IntegerField(default=0)
    date = models.DateField( auto_now_add=True)

class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=0)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="LeagueOne"),
        # message:
        email_plaintext_message,
        # from:
        "chukwuka932@gmail.com",
        # to:
        [reset_password_token.user.email]
    )