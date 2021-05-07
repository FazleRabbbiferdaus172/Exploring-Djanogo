from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'text': "upper filter test", 'num': 99}
    return render(request, 'templateLearnApp/index.html', context)


def other(request):
    return render(request, 'templateLearnApp/other.html')


def relative(request):
    return render(request, 'templateLearnApp/relative.html')
