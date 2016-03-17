from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/show/$', views.show, name='show'),
	url(r'^(?P<pk>[0-9]+)/import/$', views.download, name='download'),
]