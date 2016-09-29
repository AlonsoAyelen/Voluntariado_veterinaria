# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Sintoma(models.Model):
	nombre = models.CharField(max_length = 100)


class Propietario(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 100)
	barrio = models.CharField(max_length = 100)
	procedencia = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 100)
	edad = models.IntegerField()
	grado_de_instruccion = models.CharField(max_length = 100)
	ocupacion = models.CharField(max_length = 100)
	numero_convivientes_adultos = models.IntegerField()
	numero_convivientes_ninios = models.IntegerField()
	en_edad_escolar = models.IntegerField()
	mascotas = models.CharField(max_length = 100)
	tipos = models.CharField(max_length = 100)
	vivienda = models.CharField(max_length = 100)
	material = models.CharField(max_length = 100)
	ambientes = models.IntegerField()
	agujeros = models.CharField(max_length = 100)
	agua = models.CharField(max_length = 100)
	excretas = models.CharField(max_length = 100)
	residuos_domiciliarios = models.CharField(max_length = 100)
	recoleccion_de_residuos = models.CharField(max_length = 100)
	basural = models.CharField(max_length = 100)
	roedores = models.CharField(max_length = 100)
	agua_servida = models.CharField(max_length = 100)
	inundaciones = models.CharField(max_length = 100)
	ultima_inundacion = models.DateField(auto_now = False,null=True,blank=True)
	signos_clinicos = models.CharField(max_length = 100)
	integrante = models.CharField(max_length = 100)
	sintomas = models.ManyToManyField(Sintoma)
	aclaracion = models.CharField(max_length = 100)
	status  = models.BooleanField(default = True)
	class Meta:
		managed = True      # add this\
		app_label = 'vete' # & this
	def __unicode__(self):return self.nombre + '-' + self.apellido + '-' + self.direccion


class Analisis(models.Model):
	profesional = models.CharField(max_length = 200)
	historia_clinica = models.CharField(max_length = 200)
	fecha = models.DateField(auto_now = False)
	dilucion_inicial = models.CharField(max_length = 200)
	reactivo = models.BooleanField(default = False)
	observaciones = models.CharField(max_length = 200)


class Canino(models.Model):
	analisis = models.ForeignKey(Analisis,null=True, blank=True)
	propietario = models.ForeignKey(Propietario,null=True, blank=True)
	nombre = models.CharField(max_length = 80)
	protocolo = models.CharField(max_length = 20)
	especie = models.CharField(max_length = 40)
	sexo = models.CharField(max_length = 20)
	raza = models.CharField(max_length = 40)
	edad = models.IntegerField()
	motivo_de_consulta = models.CharField(max_length = 400)
	uso_de_la_mascota = models.CharField(max_length = 100)
	habitos = models.CharField(max_length = 200)
	contacto_con_basural = models.CharField(max_length = 40)
	caza = models.CharField(max_length = 40)
	caza_roedores = models.CharField(max_length = 40)
	observacion_roedores = models.CharField(max_length = 100)
	vacunado_contra_leptospirosis = models.CharField(max_length = 40)
	desparasitado = models.CharField(max_length = 40)
	eliminacion_de_excretas = models.CharField(max_length = 40)
	habitos_alimenticios = models.CharField(max_length = 200)
	signos_clinicos = models.CharField(max_length = 100)
	piel_Linfonodos = models.CharField(max_length = 200)
	digestivo = models.CharField(max_length = 200)
	cardio_respiratorio = models.CharField(max_length = 200)
	urogenital = models.CharField(max_length = 200)
	musculoesqueleticonervioso = models.CharField(max_length = 200)
	procedimiento_realizado = models.CharField(max_length = 200)
	peso = models.DecimalField(max_digits = 4,decimal_places = 2)
	actitud = models.CharField(max_length = 40)
	mucosas = models.CharField(max_length = 40)
	TLC = models.CharField(max_length = 40)
	hidratacion = models.CharField(max_length = 40)
	FC = models.CharField(max_length = 40)
	pulso = models.CharField(max_length = 40)
	FR = models.CharField(max_length = 40)
	T = models.DecimalField(max_digits = 5,decimal_places = 2)
	status  = models.BooleanField(default = True)
	class Meta:
		managed = True      # add this\
		app_label = 'vete' # & this
	def __unicode__(self):return self.nombre + '-' + str(self.propietario)

class Bioquimica(models.Model):
	canino = models.ForeignKey(Canino)
	fecha = models.DateField(auto_now = False)
	urea = models.DecimalField(max_digits = 5,decimal_places = 2)
	crea = models.DecimalField(max_digits = 5,decimal_places = 2)
	ALT = models.DecimalField(max_digits = 5,decimal_places = 2)
	AST = models.DecimalField(max_digits = 5,decimal_places = 2)
	PT = models.DecimalField(max_digits = 5,decimal_places = 2)
	alb = models.DecimalField(max_digits = 5,decimal_places = 2)
	FAS = models.DecimalField(max_digits = 5,decimal_places = 2)
	GGT = models.DecimalField(max_digits = 5,decimal_places = 2)
	CPK = models.DecimalField(max_digits = 5,decimal_places = 2)
	col = models.DecimalField(max_digits = 5,decimal_places = 2)
	bil_t = models.DecimalField(max_digits = 5,decimal_places = 2)
	bil_d = models.DecimalField(max_digits = 5,decimal_places = 2)
	trig = models.DecimalField(max_digits = 5,decimal_places = 2)
	varios = models.CharField(max_length = 200)
	status  = models.BooleanField(default = True)





class Hemograma(models.Model):
	canino = models.ForeignKey(Canino)
	fecha = models.DateField(auto_now = False)
	HTO = models.IntegerField()
	s_o_l = models.DecimalField(max_digits = 5,decimal_places = 2)
	GR = models.DecimalField(max_digits = 5,decimal_places = 2)
	Hb = models.DecimalField(max_digits = 5,decimal_places = 2)
	plaquetas = models.IntegerField()
	GB = models.DecimalField(max_digits = 5,decimal_places = 2)
	VCM = models.DecimalField(max_digits = 5,decimal_places = 2)
	HCM = models.DecimalField(max_digits = 5,decimal_places = 2)
	ChCM = models.DecimalField(max_digits = 5,decimal_places = 2)
	FLR_NB = models.IntegerField()
	FLR_NS = models.IntegerField()
	FLR_E = models.IntegerField()
	FLR_B = models.IntegerField()
	FLR_L = models.IntegerField()
	FLR_M = models.IntegerField()
	FLA_REF = models.IntegerField()
	FLA_NB = models.IntegerField()
	FLA_NS = models.IntegerField()
	FLA_E = models.IntegerField()
	FLA_B = models.IntegerField()
	FLA_L = models.IntegerField()
	FLA_M = models.IntegerField()
	observaciones = models.TextField()
	status  = models.BooleanField(default = True)


class Serovar(models.Model):
	serogrupo = models.CharField(max_length = 200)
	serovar = models.CharField(max_length = 200)
	cepa = models.CharField(max_length = 200)
	especie = models.CharField(max_length = 200)



