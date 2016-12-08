from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^(?P<name>[a-zA-Z0-9 ]+)/$', views.content, name='content'),
]
