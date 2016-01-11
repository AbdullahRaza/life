__author__ = 'Abdullah'

from rest_framework import serializers
from django.contrib.auth.models import User, Group
from childhood.models import Musician, Videos

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields=('url' ,'id', 'first_name', 'last_name', 'instrument')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videos
        fields=('url', 'video_id','video_name', 'video_path')
