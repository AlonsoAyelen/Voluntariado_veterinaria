from django.conf.urls import patterns, url, include
from views import form_canino_view , nuevo_usuario , login , duenios_view , nuevo_duenio_view

urlpatterns = patterns('vete.apps.home.views',
        url(r'^$','index_view',name='vista_principal'),
	url(r'^form_canino/$','form_canino_view',name='vista_canino_form'),
	url(r'^usuario/nuevo$','nuevo_usuario',name='nuevo_usuario'),
	url(r'^login$','login_view',name='login'),
	url(r'^duenios$','duenios_view',name='duenios_view'),
	url(r'^nuevo_duenio/$','nuevo_duenio_view',name='nuevo_duenio'),
)


