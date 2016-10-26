from django.conf.urls import patterns, url
from .views import ScrapDetails

urlpatterns = patterns('',
	
   url(r'^$',ScrapDetails.as_view(), name='scrap_details'),



)

