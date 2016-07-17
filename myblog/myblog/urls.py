from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','learn.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^learn/', 'learn.views.index'),
    url(r'^cal/','learn.views.cal', name = 'cal'), #/cal/?a=1&b=4
    url(r'^cal2/(\d+)/(\d+)/', 'learn.views.cal2', name = 'cal2') #/cal2/2/3/
)
