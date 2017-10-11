from django.conf.urls import url

from . import views

app_name = 'scoreboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/$', views.update, name='update'),
    url(r'^(?P<match_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^create/$', views.create, name='create'),
    url(r'^double/$', views.double, name='create'),
]