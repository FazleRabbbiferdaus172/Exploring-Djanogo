from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.


class Index_view(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injected'] = "HI!! I'M INJECTED"
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
