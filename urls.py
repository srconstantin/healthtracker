from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^tracker/$', 'tracker.views.index'),
    (r'^tracker/(?P<day_id>\d+)/$', 'tracker.views.detail'),
    (r'^tracker/results/$', 'tracker.views.results'),
    (r'^tracker/(?P<day_id>\d+)/enter/$', 'tracker.views.enter'),
    (r'^tracker/(?P<day_id>\d+)/create$', 'tracker.views.create'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
