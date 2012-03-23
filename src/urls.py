from django.conf.urls.defaults  import patterns, include, url
from django.contrib             import admin

from core.views                 import homepage

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'^inscricao/', include('subscriptions.urls', namespace='subscriptions')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


