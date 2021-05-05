from django.conf.urls import url
from myModelFormsLearnApp import views
urlpatterns = [
    url(r'^$', views.form_view, name='form'),
]
