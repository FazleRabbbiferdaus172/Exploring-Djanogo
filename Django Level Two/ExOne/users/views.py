from django.shortcuts import render
from users.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html')


def userList(request):
    users = User.objects.order_by('first_name')
    d = {'users': users}
    return render(request, 'usres/userList.html', context=d)
