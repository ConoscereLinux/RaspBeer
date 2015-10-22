from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Percorsi librerie e css
   	(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_ROOT}),
	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_ROOT}),
	(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMG_ROOT}),
	(r'^res/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.RES_ROOT}),

    
	url(r'^$', 'base.views.render_home', name='render_home'),
	url(r'^ricetta/nuova/$', 'ricette.views.render_nuova_ricetta', name='render_nuova_ricetta'),
	url(r'^ricetta/coppia/nuova/$', 'ricette.views.render_form_coppia_cottura', name='render_form_coppia_cottura'),
	url(r'^ricetta/coppia/modifica/$', 'ricette.views.render_coppia_modifica', name='render_coppia_modifica'),
	url(r'^ricetta/lista/$', 'ricette.views.render_lista_ricette', name='render_lista_ricette'),
	
	url(r'^controller/temp/$', 'controller.views.get_temperature', name='get_temperature'),
	url(r'^controller/start/ricetta/$', 'controller.views.start_cottura_ricetta', name='start_cottura_ricetta'),
	url(r'^controller/stop/cottura/$', 'controller.views.stop_cottura_ricetta', name='stop_cottura_ricetta'),
	url(r'^controller/start/$', 'controller.views.start_raspbeer', name='start_raspbeer'),
	url(r'^controller/info/$', 'controller.views.get_info', name='get_info'),
	
	
	url(r'^admin/', include(admin.site.urls)),
)
