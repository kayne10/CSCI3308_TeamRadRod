from django.conf.urls import include, url
from . import views

app_name = 'meetups'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_meetup/$', views.create_meetup, name='create_meetup'),
	url(r'^create_comment/$', views.create_comment, name='create_comment'),
	url(r'^(?P<meetup_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<meetup_id>[0-9]+)/create_comment/$', views.create_comment, name='create_comment'),
]
