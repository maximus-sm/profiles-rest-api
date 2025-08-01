from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        #password should be hidden and not shown when accessing an user info
        #write_only for not returning when get
        #style for hiding?
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self,validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    

