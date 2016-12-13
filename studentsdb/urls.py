from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    url(r'^$', 'students.views.podii', name='podii'),
    url(r'^biblioteka/$', 'students.views.biblioteka', name='biblioteka'),
    url(r'^vuhovna/$', 'students.views.vyhovna', name='vyhovna'),
    url(r'^muzey/$', 'students.views.muzey', name='muzey'),
    url(r'^kolek/$', 'students.views.kolek', name='kolek'),
    url(r'^psuholoh/$', 'students.views.psuholoh', name='psuholoh'),
    url(r'^zno/$', 'students.views.zno', name='zno'),
    url(r'^rozklad/$', 'students.views.rozklad', name='rozlad'),
    url(r'^istoria/$', 'students.views.istoria', name='istoria'),
    ###adding
    url(r'^podii_add/$', 'students.views.podii_add', name='podii_add'),



    ###edit
    url(r'^podii/(?P<pk>\d+)/edit/$',
       'students.views.podii_edit', name='podii_edit'),


    ###delete
    url(r'^podii/(?P<pk>\d+)/delete/$',
       'students.views.podii_delete', name='podii_delete'),


    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
 # serve files from media folder
 urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 'document_root': MEDIA_ROOT}))
