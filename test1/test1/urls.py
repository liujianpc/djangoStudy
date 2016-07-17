from django.conf.urls import patterns, include, url

from test1.views import index
from test1.views import fuck
from blog.views import intro
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'test1.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fuck/',fuck),
    url('^index/$',index),
    url('^blog/$',intro),
)
