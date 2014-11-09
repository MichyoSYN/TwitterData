__author__ = 'Michyo'

from django.conf.urls import patterns, url
from DataAnalyse import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^/(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^/test/$', views.test, name = 'test'),
)