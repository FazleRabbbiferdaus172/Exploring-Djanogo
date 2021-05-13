from os import name
from django.conf.urls import url
from django.contrib import admin
from BasicApp import views

app_name = 'BasicApp'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'create/$', views.SchoolCreateView.as_view(), name='create'),
]
