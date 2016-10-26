from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scraper.views.home', name='home'),
    url(r'^', include('apps.scrap.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
