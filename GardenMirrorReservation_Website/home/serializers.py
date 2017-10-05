from django.contrib.auth.models import User, Group
from home.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')

class UserProfileInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = ('contact','profile_pic',)
