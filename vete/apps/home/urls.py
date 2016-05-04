from django.conf.urls import patterns, url, include
from views import  nuevo_usuario , login , duenios_view , nuevo_duenio_view ,nuevo_canino_view , caninos_view , usuarios_view , logout , detalles_duenio_view , detalles_canino_view

urlpatterns = patterns('vete.apps.home.views',
	url(r'^usuario/nuevo$','nuevo_usuario',name='nuevo_usuario'),
	url(r'^login$','login_view',name='login'),
	url(r'^logout$','logout_view',name='logout_view'),
	url(r'^duenios$','duenios_view',name='duenios_view'),
	url(r'^nuevo_duenio/$','nuevo_duenio_view',name='nuevo_duenio'),
	url(r'^nuevo_canino/$','nuevo_canino_view',name='nuevo_canino'),
	url(r'^caninos$','caninos_view',name='caninos_view'),
	url(r'^usuarios$','usuarios_view',name='usuarios_view'),
	url(r'^detalles_duenio$','detalles_duenio_view',name='detalles_duenio_view'),
	url(r'^detalles_canino$','detalles_canino_view',name='detalles_canino_view'),

)


