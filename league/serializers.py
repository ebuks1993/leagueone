from rest_framework import serializers 
from .models import games


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
...
class UserCreateSerializer(BaseUserCreateSerializer):
 class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'email',
            'password','Gender','Date_of_birth']
    

class gameSerializer(serializers.ModelSerializer):
  class Meta:
    model=games
    fields=['id','Pitch','Address','Date','Price','meridian','Time']

 