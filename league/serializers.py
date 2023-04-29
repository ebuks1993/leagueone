from rest_framework import serializers 


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
...
class UserCreateSerializer(BaseUserCreateSerializer):
 class Meta(BaseUserCreateSerializer.Meta):
    fields = ['id', 'username', 'email',
            'password','Gender','Date_of_birth']
 