from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


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
	return render_to_response('home/duenios_view.html' , context_instance=RequestContext(request))


def nuevo_duenio_view(request):
	if(request.method == 'POST'):
		nombre = request.POST.get('nombreDuenio')
		direccion = request.POST.get('direccion')
		telefono = request.POST.get('telefono')
		barrio = request.POST.get('barrio')
		adultos = request.POST.get('convivientes_adultos')
		ninios = request.POST.get('convivientes_ninios')

	else:
		return render_to_response('home/nuevo_duenio.html' , context_instance=RequestContext(request))

