from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ejemplo.views.home', name='home'),
    # url(r'^ejemplo/', include('ejemplo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 (r'^saluda/$', 'ejemplo.saluda.views.hola'),
 (r'^fibonacci/$', 'ejemplo.fibonacci.views.funcion_fibonacci'),
 #(r'^pastebin2/$', 'ejemplo.pastebin2.views.index'),
 (r'^pastebin/', include('pastebin.urls')),
)

