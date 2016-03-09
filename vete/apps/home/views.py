from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from vete.apps.vete.models import Propietario

def index_view(request):
        return render_to_response('home/index.html',context_instance=RequestContext(request))

def form_canino_view(request):
	formulario = CaninoForm()
	ctx = {'form':formulario}
	return render_to_response('home/form_canino.html',ctx,context_instance=RequestContext(request))

@csrf_protect
def nuevo_usuario(request):
	error = ''
	if request.method == 'POST':
		nombre = request.POST.get('nombre')
		clave = request.POST.get('clave')
		claveconf = request.POST.get('clave_conf')
		tipo = request.POST.get('tipo')
		if clave == claveconf:
			user=''
			if tipo == "Clinico":	
				user = User.objects.create_user(username=nombre,password=clave,is_staff=True)
			else:
				user = User.objects.create_user(username=nombre,password=clave,is_staff=False)
			user.save()
		else:
			error = "Las claves no coinciden"
	return render_to_response('home/nuevo_usuario.html' , { 'mensaje' : error} , context_instance=RequestContext(request))


def login_view(request):
	error = ''
	nombre = request.POST.get('nombreLogin')
	clave = request.POST.get('claveLogin')
	user = authenticate(username=nombre, password=clave)
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	        return render_to_response('home/duenios_view.html' ,  context_instance=RequestContext(request))
	    else:
	        return render_to_response('home/login_view.html' ,  context_instance=RequestContext(request))
	else:
	    error = "usuario o clave incorrectos"
	return render_to_response('home/login_view.html' ,{ 'mensaje' : error }, context_instance=RequestContext(request))


def duenios_view(request):
	duenios = Propietario.objects.filter(status = True)
	contexto = {'duenios':duenios}
	return render_to_response('home/duenios_view.html' ,contexto, context_instance=RequestContext(request))


def nuevo_duenio_view(request):
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
		print ultima
		integrante = request.POST.get('integrante')
		sintomas = request.POST.get('sintomas')
		aclaracion = request.POST.get('aclaracion')
		status = True

		propietario = Propietario(nombre = nombre,apellido=apellido, direccion = direccion,barrio=barrio,procedencia=procedencia, telefono = telefono,edad=edad,grado_de_instruccion=instruccion ,ocupacion=ocupacion , numero_convivientes_adultos = adultos, numero_convivientes_ninios = ninios, en_edad_escolar=escolar , mascotas=mascotas , tipos = tipos , vivienda = vivienda , material = material , ambientes = ambientes , agujeros = agujeros ,agua = agua , excretas = excretas , residuos_domiciliarios = residuos , recoleccion_de_residuos = recoleccion , basural = basural , roedores = roedores ,agua_servida = agua_servida , inundaciones = inundaciones , ultima_inundacion = ultima , integrante = integrante , sintomas = sintomas , aclaracion = aclaracion , status = status)
		propietario.save()		
	return render_to_response('home/nuevo_duenio.html' , context_instance=RequestContext(request))

