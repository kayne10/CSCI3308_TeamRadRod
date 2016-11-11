from django.conf.urls import include, url
from . import views

app_name = 'assignments'


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_assignment/$', views.create_assignment, name='create_assignment'),
]
