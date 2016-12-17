from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.view.podii import Podii_List, PodiiCreate, PodiiUpdate, PodiiDelete




urlpatterns = patterns('',
    url(r'^$', Podii_List.as_view(), name='podii'),
    url(r'^biblioteka/$', 'students.view.biblioteka.biblioteka', name='biblioteka'),
    url(r'^vuhovna/$', 'students.view.vyhovna.vyhovna', name='vyhovna'),
    url(r'^muzey/$', 'students.view.muzey.muzey', name='muzey'),
    url(r'^kolek/$', 'students.view.kolek.kolek', name='kolek'),
    url(r'^psuholoh/$', 'students.view.psuholoh.psuholoh', name='psuholoh'),
    url(r'^zno/$', 'students.view.zno.zno', name='zno'),
    url(r'^rozklad/$', 'students.view.rozklad.rozklad', name='rozlad'),
    url(r'^istoria/$', 'students.view.istoria.istoria', name='istoria'),
    ###adding
    url(r'^podii_add/$', PodiiCreate.as_view(), name='podii_add'),



    ###edit
    url(r'^podii/(?P<pk>\d+)/edit/$',
       PodiiUpdate.as_view(), name='podii_edit'),


    ###delete
    url(r'^podii/(?P<pk>\d+)/delete/$',
       PodiiDelete.as_view(), name='podii_delete'),


    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
 # serve files from media folder
 urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 'document_root': MEDIA_ROOT}))
