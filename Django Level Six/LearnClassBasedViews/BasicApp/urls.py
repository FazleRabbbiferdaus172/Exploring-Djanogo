from django.conf.urls import url
from django.contrib import admin
from BasicApp import views

app_name = 'BasicApp'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
]
