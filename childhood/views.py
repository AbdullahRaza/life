from django.shortcuts import render_to_response


__author__ = 'Abdullah'


def home(request):
    var = 5
    return render_to_response('home.html')


def dummy(request):
    return render_to_response('dummy.html')