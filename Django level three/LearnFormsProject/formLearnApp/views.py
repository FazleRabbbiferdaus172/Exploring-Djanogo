from django.shortcuts import render
from formLearnApp import forms
# Create your views here.


def index(request):
    return render(request, 'index.html')


def form_name_view(request):
    form_view = forms.FromName()
    print('ok1')
    print("request type: ", request.method)
    if request.method == 'POST':
        print('ok2')
        form_view = forms.FromName(request.POST)
        if form_view.is_valid():
            print('ok3')
            print("Validation succesful")
            print("NAME: {}".format(form_view.cleaned_data['name']))
            print("EMAIL: {}".format(form_view.cleaned_data['email']))
            print("TEXT: {}".format(form_view.cleaned_data['text']))
    return render(request, 'form_name_view/form_name_view.html', context={'form': form_view})
