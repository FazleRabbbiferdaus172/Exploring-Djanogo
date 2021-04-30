from django.shortcuts import render
from first_app import models
# Create your views here.


def index(request):
    wp = models.AccessRecord.objects.order_by('date')
    d = {'access_record': wp}
    return render(request, 'first_app/index.html', context=d)
