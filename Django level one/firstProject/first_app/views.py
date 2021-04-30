from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    d = {'insert_me': "Hello from views.py"}
    return render(request, 'first_app/index.html', context=d)
