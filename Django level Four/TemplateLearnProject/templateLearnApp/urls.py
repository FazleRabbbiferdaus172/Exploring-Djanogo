from django.conf.urls import url
from templateLearnApp import views
app_name = 'templateLearnApp'
urlpatterns = [
    url(r'^other/', views.other, name='other'),
    url(r'^relative/', views.relative, name='relative'),
]
