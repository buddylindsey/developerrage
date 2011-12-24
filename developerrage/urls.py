from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='home'),
    url(r'^submit/$', 'comic.views.upload'),
    url(r'^about/$', 'home.views.about'),
    url(r'^(?P<comic_id>\d+)-(?P<slug>[-\w]+)/$', 'comic.views.comic'),
    # Examples:
    # url(r'^developerrage/', include('developerrage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
