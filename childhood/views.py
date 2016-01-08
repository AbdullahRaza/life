from django.shortcuts import render_to_response

from django.contrib.auth.models import User, Group
from childhood.models import Musician
from rest_framework import viewsets, permissions
from childhood.serializers import UserSerializer, GroupSerializer, MusicianSerializer


__author__ = 'Abdullah'


def home(request):
    var = 5
    return render_to_response('home.html')


def dummy(request):
    return render_to_response('dummy.html')




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    permission_classes = (permissions.AllowAny,)


