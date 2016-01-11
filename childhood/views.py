import mimetypes
import os
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, FileResponse
from django.shortcuts import render_to_response, render

from django.contrib.auth.models import User, Group
from childhood.models import Musician, Videos
from rest_framework import viewsets, permissions
from childhood.serializers import UserSerializer, GroupSerializer, MusicianSerializer, VideoSerializer


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

class VideosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.AllowAny,)


def form(request):
    return render(request, 'form.html')

def uploadfile(request):
    # for count, x in enumerate(request.FILES.getlist("files")):
    #     def process(f):
    #         with open('childhood/media/file_'+str(count),'wb+') as destination:
    #             for chunk in f.chunks():
    #                 destination.write(chunk)
    #
    #     process(x)
    videotitle=request.POST.get("videoname")
    videofile=request.FILES.get("files")
    v=Videos()
    v.video_name=videotitle
    v.video_path=videofile
    v.save()



    return HttpResponse("Files are uploaded!"+request.method)


def downloadfile(request, videoid):
    # filename="childhood/media/file_0"
    # downloadname="video.mp4"
    # wrapper=FileWrapper(file(filename,"rb"))
    # content_type=mimetypes.guess_type(filename)[0]

    # respone=HttpResponse(wrapper, content_type=content_type)
    # respone=HttpResponse(content_type=filename)
    v=Videos.objects.get(video_id=videoid)
    filename='childhood/media/'+str(v.video_path)
    response=FileResponse(open(filename,'rb'))
    response['content-length']=os.path.getsize(filename)
    response['Content-Disposition']='attachment; filename="video.mp4"'


    return response