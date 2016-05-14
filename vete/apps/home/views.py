from django.shortcuts import render_to_response , redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from vete.apps.vete.models import Propietario
from vete.apps.vete.models import Canino


@csrf_protect
def nuevo_usuario(request):
	contexto = {'mensaje':'' , 'titulo':'' , 'url_action':''}
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		contexto['titulo'] = 'Agregar usuario'
		contexto['url_action'] = request.get_full_path()
		if request.method == 'POST':
			nombre = request.POST.get('nombre')
			clave = request.POST.get('clave')
			claveconf = request.POST.get('clave_conf')
			tipo = request.POST.get('tipo')
			if clave == claveconf:
				if(len(User.objects.filter(username = nombre)) == 0):
					user=''
					if tipo == "Clinico":	
						user = User.objects.create_user(username=nombre,password=clave,is_staff=True)
					else:
						user = User.objects.create_user(username=nombre,password=clave,is_staff=False)
					user.save()
				else:
					contexto['mensaje'] = "El usuario ya existe"
			else:
				contexto['mensaje'] = "Las claves no coinciden"
		return render_to_response('home/nuevo_usuario.html' , contexto , context_instance=RequestContext(request))
	return render_to_response('home/login_view.html' , context_instance=RequestContext(request))

def login_view(request):
	if request.method == 'POST':
		error = ''
		nombre = request.POST.get('nombreLogin')
		clave = request.POST.get('claveLogin')
		user = authenticate(username=nombre, password=clave)
		if user is not None:
		    # the password verified for the user
		    if user.is_active:
		    	login(request,user)
		        return redirect('/duenios' )
		    else:
		        return render_to_response('home/login_view.html' ,  context_instance=RequestContext(request))
		else:
			error = "Usuario o clave incorrectos"
			return render_to_response('home/login_view.html' ,{ 'mensaje' : error }, context_instance=RequestContext(request))
	else:
		return render_to_response('home/login_view.html' , context_instance=RequestContext(request))

def duenios_view(request):
	contexto = {'titulo':'' , 'nombre':'','apellido':'','direccion':'','barrio':'','procedencia':'','telefono':'','edad':'','instruccion':'','ocupacion':'','adultos':'','ninios':'','escolar':'','mascotas':'','tipos':'','vivienda':'','material':'','ambientes':'','agujeros':'','agua':'','excretas':'','residuos':'','recoleccion':'','basural':'','roedores':'','agua_servida':'','inundaciones':'','ultima':'','integrante':'','sintomas':'','aclaracion':''}
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		duenios = Propietario.objects.filter()
		contexto = {'duenios':duenios}
		if(len(request.POST.getlist('eliminar'))> 0):
			duenio = Propietario.objects.filter(id = int(request.POST.getlist('eliminar')[0]))
			duenio.delete()
			duenios = Propietario.objects.filter()
			contexto = {'duenios':duenios}
	return render_to_response('home/duenios_view.html' ,contexto, context_instance=RequestContext(request))



def detalles_duenio_view(request):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		contexto = {'nombre':'','apellido':'','direccion':'','barrio':'','procedencia':'','telefono':'','edad':'','instruccion':'','ocupacion':'','adultos':'','ninios':'','escolar':'','mascotas':'','tipos':'','vivienda':'','material':'','ambientes':'','agujeros':'','agua':'','excretas':'','residuos':'','recoleccion':'','basural':'','roedores':'','agua_servida':'','inundaciones':'','ultima':'','integrante':'','sintomas':'','aclaracion':''}
		if(len(request.POST.getlist('mas'))> 0):
			duenio = Propietario.objects.filter(id = int(request.POST.getlist('mas')[0]))
			contexto['nombre'] = duenio[0].nombre
			contexto['apellido'] = duenio[0].apellido
			contexto['direccion'] = duenio[0].direccion
			contexto['barrio'] = duenio[0].barrio
			contexto['procedencia'] = duenio[0].procedencia
			contexto['telefono'] = duenio[0].telefono
			contexto['edad'] = duenio[0].edad
			contexto['instruccion'] = duenio[0].grado_de_instruccion
			contexto['ocupacion'] = duenio[0].ocupacion
			contexto['adultos'] = duenio[0].numero_convivientes_adultos
			contexto['ninios'] = duenio[0].numero_convivientes_ninios
			contexto['escolar'] = duenio[0].en_edad_escolar
			contexto['mascotas'] = duenio[0].mascotas
			contexto['tipos'] = duenio[0].tipos
			contexto['vivienda'] = duenio[0].vivienda
			contexto['material'] = duenio[0].material
			contexto['ambientes'] = duenio[0].ambientes
			contexto['agujeros'] = duenio[0].agujeros
			contexto['agua'] = duenio[0].agua
			contexto['excretas'] = duenio[0].excretas
			contexto['residuos'] = duenio[0].residuos_domiciliarios
			contexto['recoleccion'] = duenio[0].recoleccion_de_residuos
			contexto['basural'] = duenio[0].basural
			contexto['roedores'] = duenio[0].roedores
			contexto['agua_servida'] = duenio[0].agua_servida
			contexto['inundaciones'] = duenio[0].inundaciones
			contexto['ultima'] = duenio[0].ultima_inundacion
			contexto['integrante'] = duenio[0].integrante
			contexto['sintomas'] = duenio[0].sintomas
			contexto['aclaracion'] = duenio[0].aclaracion
		return render_to_response('home/ficha_duenio.html' ,contexto, context_instance=RequestContext(request))


def detalles_canino_view(request):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		contexto = {'propietario':'' , 'nombre':'' ,'especie':'', 'sexo':'','raza':'','edad':'','motivo_de_consulta':'', 'uso_de_la_mascota':'','habitos':'' , 'contacto_con_basural':'' , 'caza':'','caza_roedores':'' ,	'observacion_roedores':'', 'vacunado_contra_leptospirosis':'','desparasitado':'' , 'eliminacion_de_excretas':'',	'habitos_alimenticios':'','signos_clinicos':'','piel_Linfonodos':'','digestivo':'','cardio_respiratorio':'','urogenital':'','musculoesqueleticonervioso':'','procedimiento_realizado':'','peso':'','actitud':'','mucosas':'','TLC':'','hidratacion':'','FC':'','pulso':'','FR':'','T':''}
		if(len(request.POST.getlist('mas'))> 0):
			canino = Canino.objects.filter(id = int(request.POST.getlist('mas')[0]))
			contexto['propietario'] = canino[0].propietario 
			contexto['nombre'] = canino[0].nombre
			contexto['especie'] = canino[0].especie
			contexto['sexo'] = canino[0].sexo
			contexto['raza'] = canino[0].raza
			contexto['edad'] = canino[0].edad
			contexto['motivo_de_consulta'] = canino[0].motivo_de_consulta
			contexto['uso_de_la_mascota'] = canino[0].uso_de_la_mascota
			contexto['habitos'] = canino[0].habitos
			contexto['contacto_con_basural'] = canino[0].contacto_con_basural
			contexto['caza'] = canino[0].caza
			contexto['caza_roedores'] = canino[0].caza_roedores
			contexto['observacion_roedores'] = canino[0].observacion_roedores
			contexto['vacunado_contra_leptospirosis'] = canino[0].vacunado_contra_leptospirosis
			contexto['desparasitado'] = canino[0].desparasitado
			contexto['eliminacion_de_excretas'] = canino[0].eliminacion_de_excretas
			contexto['habitos_alimenticios'] = canino[0].habitos_alimenticios
			contexto['signos_clinicos'] = canino[0].signos_clinicos
			contexto['piel_Linfonodos'] = canino[0].piel_Linfonodos
			contexto['digestivo'] = canino[0].digestivo
			contexto['cardio_respiratorio'] = canino[0].cardio_respiratorio
			contexto['urogenital'] = canino[0].urogenital
			contexto['musculoesqueleticonervioso'] = canino[0].musculoesqueleticonervioso
			contexto['procedimiento_realizado'] = canino[0].procedimiento_realizado
			contexto['peso'] = canino[0].peso
			contexto['actitud'] = canino[0].actitud
			contexto['mucosas'] = canino[0].mucosas
			contexto['TLC'] = canino[0].TLC
			contexto['hidratacion'] = canino[0].hidratacion
			contexto['FC'] = canino[0].FC
			contexto['pulso'] = canino[0].pulso
			contexto['FR'] = canino[0].FR
			contexto['T'] = canino[0].T
		return render_to_response('home/ficha_canino.html' ,contexto, context_instance=RequestContext(request))


def caninos_view(request):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		caninos = Canino.objects.all()
		contexto = {'titulo':'','caninos':caninos,'propietario':'' , 'nombre':'' ,'especie':'', 'sexo':'','raza':'','edad':'','motivo_de_consulta':'', 'uso_de_la_mascota':'','habitos':'' , 'contacto_con_basural':'' , 'caza':'','caza_roedores':'' ,	'observacion_roedores':'', 'vacunado_contra_leptospirosis':'','desparasitado':'' , 'eliminacion_de_excretas':'',	'habitos_alimenticios':'','signos_clinicos':'','piel_Linfonodos':'','digestivo':'','cardio_respiratorio':'','urogenital':'','musculoesqueleticonervioso':'','procedimiento_realizado':'','peso':'','actitud':'','mucosas':'','TLC':'','hidratacion':'','FC':'','pulso':'','FR':'','T':''}
		if(len(request.POST.getlist('eliminar'))> 0):
			canino = Canino.objects.filter(id = int(request.POST.getlist('eliminar')[0]))
			canino.delete()
			caninos = Canino.objects.all()
			contexto = {'caninos':caninos}			
	return render_to_response('home/caninos_view.html' ,contexto, context_instance=RequestContext(request))

def usuarios_view(request):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		usuarios = User.objects.filter()
		contexto = {'usuarios':usuarios}
		if(len(request.POST.getlist('eliminar'))> 0):
			usuario = User.objects.filter(id = int(request.POST.getlist('eliminar')[0]))
			usuario.delete()
			usuarios = User.objects.filter()
			contexto = {'usuarios':usuarios}
	return render_to_response('home/usuarios_view.html' ,contexto, context_instance=RequestContext(request))

def actualizar_usuario_view(request,pk):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		usuarios = User.objects.all()
		usuario = User.objects.filter(id = int(pk))
		if(request.method == 'POST'):
			nombre = request.POST.get('nombre')
			clave = request.POST.get('clave')
			claveconf = request.POST.get('clave_conf')
			tipo = request.POST.get('tipo')
			if tipo == "Clinico":
				usuario.update(username=nombre , is_staff=True)
			else:
				usuario.update(username=nombre , is_staff=False)
			return render_to_response('home/usuarios_view.html' ,{'usuarios':usuarios}, context_instance=RequestContext(request))
		usuarios = User.objects.filter()	    
		return render_to_response('home/nuevo_usuario.html' ,{'usuario':usuario[0],'usuarios':usuarios,'titulo':'Modificar usuario', 'url_action':request.get_full_path()}, context_instance=RequestContext(request))




def logout_view(request):
    logout(request)
    return render_to_response('home/login_view.html', context_instance=RequestContext(request))

def nuevo_duenio_view(request):
	contexto = {'titulo':'','url_action':'','nombre':'','apellido':'','direccion':'','barrio':'','procedencia':'','telefono':'','edad':'','instruccion':'','ocupacion':'','adultos':'','ninios':'','escolar':'','mascotas':'','tipos':'','vivienda':'','material':'','ambientes':'','agujeros':'','agua':'','excretas':'','residuos':'','recoleccion':'','basural':'','roedores':'','agua_servida':'','inundaciones':'','ultima':'','integrante':'','sintomas':'','aclaracion':''}
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		contexto['titulo'] = 'Agregar duenio'
		contexto['url_action'] = request.get_full_path()
		if(request.method == 'POST'):
			nombre = request.POST.get('nombreDuenio')
			apellido = request.POST.get('apellido')
			direccion = request.POST.get('direccion')
			barrio = request.POST.get('barrio')
			procedencia = request.POST.get('procedencia')
			telefono = request.POST.get('telefono')
			edad = request.POST.get('edad')
			instruccion = request.POST.get('grado_de_instruccion')
			ocupacion = request.POST.get('ocupacion')
			adultos = request.POST.get('convivientes_adultos')
			ninios = request.POST.get('convivientes_ninios')
			escolar = request.POST.get('en_edad_escolar')
			mascotas = request.POST.get('mascotas')
			tipos = request.POST.get('tipos')
			vivienda = request.POST.get('vivienda')
			material = request.POST.get('material')
			ambientes = request.POST.get('ambientes')
			agujeros = request.POST.get('agujeros')
			agua = request.POST.get('agua')
			excretas = request.POST.get('excretas')
			residuos = request.POST.get('residuos_domiciliarios')
			recoleccion = request.POST.get('recoleccion_de_residuos')
			basural = request.POST.get('basural')
			roedores = request.POST.get('roedores')
			agua_servida = request.POST.get('agua_servida')
			inundaciones = request.POST.get('inundaciones')
			ultima = request.POST.get('ultima_inundacion')
			integrante = request.POST.get('integrante')
			sintomas = request.POST.get('sintomas')
			aclaracion = request.POST.get('aclaracion')
			status = True
			
			if(len(Propietario.objects.filter(nombre=nombre ,apellido=apellido,status=True))>0):
				contexto['error'] = "El propietario ya existe"
				contexto['nombre'] = nombre
				contexto['apellido'] = apellido
				contexto['direccion'] = direccion
				contexto['barrio'] = barrio
				contexto['procedencia'] = procedencia
				contexto['telefono'] = telefono
				contexto['edad'] = edad
				contexto['instruccion'] = instruccion
				contexto['ocupacion'] = ocupacion
				contexto['adultos'] = adultos
				contexto['ninios'] = ninios
				contexto['escolar'] = escolar
				contexto['mascotas'] = mascotas
				contexto['tipos'] = tipos
				contexto['vivienda'] = vivienda
				contexto['material'] = material
				contexto['ambientes'] = ambientes
				contexto['agujeros'] = agujeros
				contexto['agua'] = agua
				contexto['excretas'] = excretas
				contexto['residuos'] = residuos
				contexto['recoleccion'] = recoleccion
				contexto['basural'] = basural
				contexto['roedores'] = roedores
				contexto['agua_servida'] = agua_servida
				contexto['inundaciones'] = inundaciones
				contexto['ultima'] = ultima
				contexto['integrante'] = integrante
				contexto['sintomas'] = sintomas
				contexto['aclaracion'] = aclaracion	
			else:
				propietario = Propietario(nombre = nombre,apellido=apellido, direccion = direccion,barrio=barrio,procedencia=procedencia, telefono = telefono,edad=edad,grado_de_instruccion=instruccion ,ocupacion=ocupacion , numero_convivientes_adultos = adultos, numero_convivientes_ninios = ninios, en_edad_escolar=escolar , mascotas=mascotas , tipos = tipos , vivienda = vivienda , material = material , ambientes = ambientes , agujeros = agujeros ,agua = agua , excretas = excretas , residuos_domiciliarios = residuos , recoleccion_de_residuos = recoleccion , basural = basural , roedores = roedores ,agua_servida = agua_servida , inundaciones = inundaciones , ultima_inundacion = ultima , integrante = integrante , sintomas = sintomas , aclaracion = aclaracion , status = status)
				propietario.save()
		return render_to_response('home/nuevo_duenio.html' ,contexto, context_instance=RequestContext(request))

def actualizar_duenio_view(request,pk):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		duenios = Propietario.objects.all()
		duenio = Propietario.objects.filter(id = int(pk))
		if(request.method == 'POST'):
			nombre = request.POST.get('nombreDuenio')
			apellido = request.POST.get('apellido')
			direccion = request.POST.get('direccion')
			barrio = request.POST.get('barrio')
			procedencia = request.POST.get('procedencia')
			telefono = request.POST.get('telefono')
			edad = request.POST.get('edad')
			instruccion = request.POST.get('grado_de_instruccion')
			ocupacion = request.POST.get('ocupacion')
			adultos = request.POST.get('convivientes_adultos')
			ninios = request.POST.get('convivientes_ninios')
			escolar = request.POST.get('en_edad_escolar')
			mascotas = request.POST.get('mascotas')
			tipos = request.POST.get('tipos')
			vivienda = request.POST.get('vivienda')
			material = request.POST.get('material')
			ambientes = request.POST.get('ambientes')
			agujeros = request.POST.get('agujeros')
			agua = request.POST.get('agua')
			excretas = request.POST.get('excretas')
			residuos = request.POST.get('residuos_domiciliarios')
			recoleccion = request.POST.get('recoleccion_de_residuos')
			basural = request.POST.get('basural')
			roedores = request.POST.get('roedores')
			agua_servida = request.POST.get('agua_servida')
			inundaciones = request.POST.get('inundaciones')
			ultima = request.POST.get('ultima_inundacion')
			integrante = request.POST.get('integrante')
			sintomas = request.POST.get('sintomas')
			aclaracion = request.POST.get('aclaracion')
			duenio.update(nombre = nombre,apellido=apellido, direccion = direccion,barrio=barrio,procedencia=procedencia, telefono = telefono,edad=edad,grado_de_instruccion=instruccion ,ocupacion=ocupacion , numero_convivientes_adultos = adultos, numero_convivientes_ninios = ninios, en_edad_escolar=escolar , mascotas=mascotas , tipos = tipos , vivienda = vivienda , material = material , ambientes = ambientes , agujeros = agujeros ,agua = agua , excretas = excretas , residuos_domiciliarios = residuos , recoleccion_de_residuos = recoleccion , basural = basural , roedores = roedores ,agua_servida = agua_servida , inundaciones = inundaciones , ultima_inundacion = ultima , integrante = integrante , sintomas = sintomas , aclaracion = aclaracion)
			# hacer redirect
			return render_to_response('home/duenios_view.html' ,{'duenios':duenios}, context_instance=RequestContext(request))
	
		return render_to_response('home/nuevo_duenio.html' ,{'duenio':duenio[0] , 'titulo':'Modificar duenio', 'url_action':request.get_full_path()}, context_instance=RequestContext(request))
		

def nuevo_canino_view(request):
	contexto = {'titulo':'','url_action':'','error':'','propietario':'' , 'nombre':'' ,'especie':'', 'sexo':'','raza':'','edad':'','motivo_de_consulta':'', 'uso_de_la_mascota':'1','habitos':'' , 'contacto_con_basural':'' , 'caza':'','caza_roedores':'' ,	'observacion_roedores':'', 'vacunado_contra_leptospirosis':'','desparasitado':'' , 'eliminacion_de_excretas':'',	'habitos_alimenticios':'','signos_clinicos':'','piel_Linfonodos':'','digestivo':'','cardio_respiratorio':'','urogenital':'','musculoesqueleticonervioso':'','procedimiento_realizado':''}
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		contexto['titulo'] = 'Agregar canino'
		contexto['url_action'] = request.get_full_path()
		if(request.method == 'POST'): 
			propietario = Propietario.objects.filter(id = int(request.POST.get('duenio')))[0]
			nombre = request.POST.get('nombreCanino')
			especie = request.POST.get('especie')
			sexo = request.POST.get('sexo')
			raza = request.POST.get('raza')
			edad = request.POST.get('edad')
			motivo_de_consulta = request.POST.get('motivo_de_consulta')
			uso_de_la_mascota = request.POST.get('uso_de_la_mascota')
			habitos = request.POST.get('habitos')
			contacto_con_basural = request.POST.get('contacto_con_basural')
			caza = request.POST.get('caza')
			caza_roedores = request.POST.get('caza_roedores')
			observacion_roedores = request.POST.get('observacion_roedores')
			vacunado_contra_leptospirosis = request.POST.get('vacunado_contra_leptospirosis')
			desparasitado = request.POST.get('desparasitado')
			eliminacion_de_excretas = request.POST.get('eliminacion_de_excretas')
			habitos_alimenticios = request.POST.get('habitos_alimenticios')
			signos_clinicos = request.POST.get('signos_clinicos')
			piel_Linfonodos = request.POST.get('piel_Linfonodos')
			digestivo = request.POST.get('digestivo')
			cardio_respiratorio = request.POST.get('cardio_respiratorio')
			urogenital = request.POST.get('urogenital')
			musculoesqueleticonervioso = request.POST.get('musculoesqueleticonervioso')
			peso = request.POST.get('peso')
			print request.POST.get('peso')
			actitud = request.POST.get('actitud')
			mucosas = request.POST.get('mucosas')
			TLC = request.POST.get('TLC')
			hidratacion = request.POST.get('hidratacion')
			FC = request.POST.get('FC')
			pulso = request.POST.get('pulso')
			FR = request.POST.get('FR')
			T = request.POST.get('T')
			procedimiento_realizado = request.POST.get('procedimiento_realizado')
			if(len(Canino.objects.filter(nombre=nombre,status=True))>0):
				contexto['error'] = "El canino ya existe"
				contexto['propietario'] = propietario 
				contexto['nombre'] = nombre
				contexto['especie'] = especie
				contexto['sexo'] = sexo
				contexto['raza'] = raza
				contexto['edad'] = edad
				contexto['motivo_de_consulta'] = motivo_de_consulta
				contexto['uso_de_la_mascota'] = uso_de_la_mascota
				contexto['habitos'] = habitos
				contexto['contacto_con_basural'] = contacto_con_basural
				contexto['caza'] = caza
				contexto['caza_roedores'] = caza_roedores
				contexto['observacion_roedores'] = observacion_roedores
				contexto['vacunado_contra_leptospirosis'] = vacunado_contra_leptospirosis
				contexto['desparasitado'] = desparasitado
				contexto['eliminacion_de_excretas'] = eliminacion_de_excretas
				contexto['habitos_alimenticios'] = habitos_alimenticios
				contexto['signos_clinicos'] = signos_clinicos
				contexto['piel_Linfonodos'] = piel_Linfonodos
				contexto['digestivo'] = digestivo
				contexto['cardio_respiratorio'] = cardio_respiratorio
				contexto['urogenital'] = urogenital
				contexto['musculoesqueleticonervioso'] = musculoesqueleticonervioso
				contexto['peso'] = peso
				contexto['actitud'] = actitud
				contexto['mucosas'] = mucosas
				contexto['TLC'] = TLC
				contexto['hidratacion'] = hidratacion
				contexto['FC'] = FC
				contexto['pulso'] = pulso
				contexto['FR'] = FR
				contexto['T'] = T
				contexto['procedimiento_realizado'] = procedimiento_realizado
			else:
				canino = Canino(propietario = propietario , nombre = nombre, especie = especie , sexo=sexo , raza = raza , edad=edad , motivo_de_consulta = motivo_de_consulta, uso_de_la_mascota=uso_de_la_mascota , habitos = habitos , contacto_con_basural = contacto_con_basural , caza = caza , caza_roedores = caza_roedores , observacion_roedores = observacion_roedores , vacunado_contra_leptospirosis = vacunado_contra_leptospirosis , desparasitado = desparasitado , eliminacion_de_excretas = eliminacion_de_excretas , habitos_alimenticios = habitos_alimenticios , signos_clinicos = signos_clinicos , piel_Linfonodos = piel_Linfonodos , digestivo = digestivo , cardio_respiratorio = cardio_respiratorio , urogenital = urogenital , musculoesqueleticonervioso = musculoesqueleticonervioso ,peso = peso,actitud = actitud,mucosas = mucosas,TLC = TLC,hidratacion = hidratacion, FC = FC, pulso = pulso, FR = FR,T = T, procedimiento_realizado = procedimiento_realizado , status = True)
				canino.save()	
		duenios = Propietario.objects.filter()
		contexto['duenios'] = duenios
		return render_to_response('home/nuevo_canino.html' ,contexto ,context_instance=RequestContext(request))		


def actualizar_canino_view(request,pk):
	if not request.user.is_authenticated():
		return redirect('login')
	else:
		caninos = Canino.objects.all()
		canino = Canino.objects.filter(id = int(pk))
		if(request.method == 'POST'):
			propietario = Propietario.objects.filter(id = int(request.POST.get('duenio')))[0]
			nombre = request.POST.get('nombreCanino')
			especie = request.POST.get('especie')
			sexo = request.POST.get('sexo')
			raza = request.POST.get('raza')
			edad = request.POST.get('edad')
			motivo_de_consulta = request.POST.get('motivo_de_consulta')
			uso_de_la_mascota = request.POST.get('uso_de_la_mascota')
			habitos = request.POST.get('habitos')
			contacto_con_basural = request.POST.get('contacto_con_basural')
			caza = request.POST.get('caza')
			caza_roedores = request.POST.get('caza_roedores')
			observacion_roedores = request.POST.get('observacion_roedores')
			vacunado_contra_leptospirosis = request.POST.get('vacunado_contra_leptospirosis')
			desparasitado = request.POST.get('desparasitado')
			eliminacion_de_excretas = request.POST.get('eliminacion_de_excretas')
			habitos_alimenticios = request.POST.get('habitos_alimenticios')
			signos_clinicos = request.POST.get('signos_clinicos')
			piel_Linfonodos = request.POST.get('piel_Linfonodos')
			digestivo = request.POST.get('digestivo')
			cardio_respiratorio = request.POST.get('cardio_respiratorio')
			urogenital = request.POST.get('urogenital')
			musculoesqueleticonervioso = request.POST.get('musculoesqueleticonervioso')
			peso = request.POST.get('peso')
			actitud = request.POST.get('actitud')
			mucosas = request.POST.get('mucosas')
			TLC = request.POST.get('TLC')
			hidratacion = request.POST.get('hidratacion')
			FC = request.POST.get('FC')
			pulso = request.POST.get('pulso')
			FR = request.POST.get('FR')
			T = request.POST.get('T')
			procedimiento_realizado = request.POST.get('procedimiento_realizado')
			canino.update(propietario = propietario , nombre = nombre, especie = especie , sexo=sexo , raza = raza , edad=edad , motivo_de_consulta = motivo_de_consulta, uso_de_la_mascota=uso_de_la_mascota , habitos = habitos , contacto_con_basural = contacto_con_basural , caza = caza , caza_roedores = caza_roedores , observacion_roedores = observacion_roedores , vacunado_contra_leptospirosis = vacunado_contra_leptospirosis , desparasitado = desparasitado , eliminacion_de_excretas = eliminacion_de_excretas , habitos_alimenticios = habitos_alimenticios , signos_clinicos = signos_clinicos , piel_Linfonodos = piel_Linfonodos , digestivo = digestivo , cardio_respiratorio = cardio_respiratorio , urogenital = urogenital , musculoesqueleticonervioso = musculoesqueleticonervioso ,peso = peso,actitud = actitud,mucosas = mucosas,TLC = TLC,hidratacion = hidratacion, FC = FC, pulso = pulso, FR = FR,T = T, procedimiento_realizado = procedimiento_realizado , status = True)
			return render_to_response('home/caninos_view.html' ,{'caninos':caninos}, context_instance=RequestContext(request))
		duenios = Propietario.objects.filter()	    
		return render_to_response('home/nuevo_canino.html' ,{'canino':canino[0],'duenios':duenios,'titulo':'Modificar canino', 'url_action':request.get_full_path()}, context_instance=RequestContext(request))

def nuevo_bioquimica_view(request):
	pass
	return render_to_response('home/nuevo_bioquimica.html' , context_instance=RequestContext(request))

def nuevo_hemograma_view(request):
	pass
	return render_to_response('home/nuevo_hemograma.html' , context_instance=RequestContext(request))