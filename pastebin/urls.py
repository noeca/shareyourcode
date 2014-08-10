from django.conf.urls.defaults import *

from models import ptb

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.create_update.create_object', { 'model': ptb }, name='ptb_agregar'),
    url(r'^ptb/edit/(?P<object_id>\d+)$', 'django.views.generic.create_update.update_object', { 'model': ptb }, name='ptb_edit'),
    url(r'^ptb/borrar/(?P<object_id>\d+)$', 'django.views.generic.create_update.delete_object', { 'model': ptb, 'post_delete_redirect': '/pastebin/' }, name='ptb_borrar'),
    url(r'^ptb/(?P<object_id>\d+)$', 'django.views.generic.list_detail.object_detail', { 'queryset': ptb.objects.all() }, name='ptb_detalle'),
    url(r'^ptb/$', 'django.views.generic.list_detail.object_list', { 'queryset': ptb.objects.all() }, name='ptb_listado'),
)
