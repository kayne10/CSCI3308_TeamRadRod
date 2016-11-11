from django.conf.urls import include, url
from . import views

app_name = 'courses'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_course/$', views.create_course, name='create_course'),
]
