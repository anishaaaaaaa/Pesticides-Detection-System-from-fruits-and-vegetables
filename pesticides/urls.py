from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home', views.home),
    url(r'info', views.info),
    url(r'blog', views.blog),
    url(r'about', views.about),
    url(r'contact', views.contact),
    url(r'temp-humi', views.temphumi)
]