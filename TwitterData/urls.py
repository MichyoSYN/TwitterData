from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TwitterData.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^DataAnalyse/', include('DataAnalyse.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^detail/', include(admin.site.urls)),
)
