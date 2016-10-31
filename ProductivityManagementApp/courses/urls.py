from django.conf.urls import include, url
from . import views

app_name = 'courses'


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^$', views.index, name='index'),
]
