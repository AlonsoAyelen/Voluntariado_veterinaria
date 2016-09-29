#from django.conf.urls import patterns, url, include
from views import  nuevo_usuario , login_view , duenios_view , nuevo_duenio_view ,nuevo_canino_view , caninos_view , usuarios_view , logout_view , detalles_duenio_view , detalles_canino_view,actualizar_duenio_view,actualizar_canino_view,actualizar_usuario_view,nuevo_bioquimica_view,nuevo_hemograma_view,bioquimicas_view,hemogramas_view , detalles_hemograma_view , detalles_bioquimica_view , actualizar_bioquimica_view , actualizar_hemograma_view , generar_pdf_view , estadisticas_view , analisis_view , index_view
from django.conf.urls import url
from django.contrib import admin
import vete.apps.home.views
urlpatterns = [
	url(r'^$', index_view , name='index'),
	url(r'^usuario/nuevo/$',nuevo_usuario,name='nuevo_usuario'),
	url(r'^login/$',login_view,name='login'),
	url(r'^logout/$',logout_view,name='logout'),
	url(r'^duenios/$',duenios_view,name='duenios_view'),
	url(r'^duenio/$',duenios_view,name='duenios_view'),
	url(r'^nuevo_duenio/$',nuevo_duenio_view,name='nuevo_duenio'),
	url(r'^actualizar_duenio/(?P<pk>[0-9]+)/$', actualizar_duenio_view, name='actualizar_duenio'),
	url(r'^actualizar_usuario/(?P<pk>[0-9]+)/$', actualizar_usuario_view, name='actualizar_usuario'),
	url(r'^actualizar_canino/(?P<pk>[0-9]+)/$', actualizar_canino_view, name='actualizar_canino'),
	url(r'^actualizar_bioquimica/(?P<pk>[0-9]+)/$', actualizar_bioquimica_view, name='actualizar_bioquimica'),
	url(r'^actualizar_hemograma/(?P<pk>[0-9]+)/$', actualizar_hemograma_view, name='actualizar_hemograma'),
	url(r'^nuevo_canino/$',nuevo_canino_view,name='nuevo_canino'),
	url(r'^caninos$',caninos_view,name='caninos_view'),
	url(r'^usuarios$',usuarios_view,name='usuarios_view'),
	url(r'^duenio/detalles_duenio$',detalles_duenio_view,name='detalles_duenio_view'),
	url(r'^detalles_canino$',detalles_canino_view,name='detalles_canino_view'),
	url(r'^hemogramas/detalles_hemograma$',detalles_hemograma_view,name='detalles_hemograma_view'),
	url(r'^bioquimicas/detalles_bioquimica$',detalles_bioquimica_view,name='detalles_bioquimica_view'),
	url(r'^nuevo_bioquimica/$',nuevo_bioquimica_view,name='nuevo_bioquimica'),
	url(r'^nuevo_hemograma/$',nuevo_hemograma_view,name='nuevo_hemograma'),
	url(r'^hemogramas/$',hemogramas_view,name='hemogramas'),
	url(r'^bioquimicas/$',bioquimicas_view,name='bioquimicas'),
	url(r'^pdf/(?P<pk>[0-9]+)/$',generar_pdf_view,name='generar_pdf'),
	url(r'^estadisticas/$',estadisticas_view,name='estadisticas'),
	url(r'^analisis/(?P<pk>[0-9]+)/$',analisis_view,name='analisis'),
]


