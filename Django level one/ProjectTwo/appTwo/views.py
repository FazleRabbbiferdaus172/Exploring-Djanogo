from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test(request):
    return HttpResponse("<em> My second App </em>")


def help(request):
    return render(request, 'appTwo/help.html')
