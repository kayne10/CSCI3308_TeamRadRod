from django.conf.urls import include, url
from . import views

app_name = 'meetups'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_meetup/$', views.create_meetup, name='create_meetup'),
]
