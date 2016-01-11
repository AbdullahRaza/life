"""life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from childhood import views

router =routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
router.register(r'musicians',views.MusicianViewSet)
router.register(r'videos',views.VideosViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'childhood.views.home'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^form/','childhood.views.form'),
    url(r'^uploadfile/','childhood.views.uploadfile'),
    url(r'^downloadfile/(?P<videoid>[0-9]+)/','childhood.views.downloadfile'),

]
