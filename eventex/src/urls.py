from django.conf.urls.defaults  import patterns, include, url
from core.views                 import homepage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage), # Url vazia, a index do site
    (r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
