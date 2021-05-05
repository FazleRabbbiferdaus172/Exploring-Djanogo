from django.shortcuts import render
from myModelFormsLearnApp import forms
# Create your views here.


def index(request):
    return render(request, 'index.html')


def form_view(request):
    form = forms.SignUpForm()
    print(request.method, "okokokok")
    if request.method == 'POST':
        print("***OK***")
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'myModelFormsLearnApp/form.html', context={'form': form})
