from rest_framework import serializers 
from .models import Games,GameSelect


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
...
class UserCreateSerializer(BaseUserCreateSerializer):
 class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'email',
            'password','Gender','Date_of_birth']
    

class gameSerializer(serializers.ModelSerializer):
  pitch=serializers.StringRelatedField()
  sport=serializers.StringRelatedField()
  Agerange=serializers.StringRelatedField()
  priz=serializers.SerializerMethodField(method_name='price')
  address=serializers.SerializerMethodField(method_name='addy')
  remain=serializers.SerializerMethodField(method_name="spotrem")
  name=serializers.SerializerMethodField(method_name="player")
  pitchmap=serializers.SerializerMethodField(method_name="pitchmapped")
  # gender=serializers.SerializerMethodField(method_name="gen")
  class Meta:
    model=Games
    fields=['id','pitch','sport','Agerange','Date','meridian','Time','Status','priz','address',"spot","remain","name","pitchmap"]

  def price(self,game:Games):
    return game.pitch.Price
  
  def addy(self,game:Games):
    return game.pitch.Address
  
  def pitchmapped(self,game:Games):
      return game.pitch.pitchmap
  
  def spotrem(self,game:Games):
    return game.pitch.players - game.spot

  def player(self,game:Games):
    return[{"name":item.user.username,"gender":item.user.Gender,"email":item.user.email} for item in game.gameselect_set.all()]
  
  # def gen(self,game:Games):
  #   return[item.user.Gender for item in game.gameselect_set.all()]


class yourgameSeralizer(serializers.ModelSerializer):
  gamdat=serializers.SerializerMethodField(method_name="gamedate")
  class Meta:
    model=GameSelect
    fields=['id','user','games','Amount',"gamdat"]


  def gamedate(self,sel:GameSelect):
    return sel.games.Date

  