from django.conf.urls.defaults  import patterns, include, url
from core.views                 import homepage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'^inscricao/', include('subscriptions.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
