from django.conf.urls import url, include
from django.contrib import admin

from main.api import urls as apiURLs


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',
    	include(apiURLs)),
]
