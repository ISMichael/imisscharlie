from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'i_miss_charlie.views.home', name='home'),
    # url(r'^i_miss_charlie/', include('i_miss_charlie.foo.urls')),
    url(r'^$', 'counter.views.index'),
    url(r'^counter/$', 'counter.views.index'), 
    url(r'^charlieishere/$', 'counter.views.charlieishere'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
