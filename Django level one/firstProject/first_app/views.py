from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        'forecasts': [
            {'ser': 1, 'date': '01-01-2021', 'temp': '21', 'humidity': '70%'},
            {'ser': 2, 'date': '02-01-2021', 'temp': '21.5', 'humidity': '73%'},
            {'ser': 3, 'date': '03-01-2021', 'temp': '22', 'humidity': '74%'},
            # etc ...
        ]
    }
    return render(request, 'first_app/index.html', context=context)
