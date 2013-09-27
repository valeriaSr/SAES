#encoding:utf-8
#from principal.models import Bebida,Receta
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def profesor_main(request):
    return render_to_response('profesor/main.html',context_instance=RequestContext(request))

def profesor_miperfil(request):
    return render_to_response('profesor/mi-perfil.html',context_instance=RequestContext(request))

def profesor_preferencias(request):
    return render_to_response('profesor/preferencias.html',context_instance=RequestContext(request))

def profesor_logout(request):
    return render_to_response('profesor/logout.html',context_instance=RequestContext(request))

def profesor_mis_grupos(request):
    return render_to_response('profesor/mis-grupos.html',context_instance=RequestContext(request))

def profesor_registrar_calificaciones(request):
    return render_to_response('profesor/registrar-calificaciones.html',context_instance=RequestContext(request))

def directorio(request):
    return render_to_response('directorio.html',context_instance=RequestContext(request))

def profesor_reportes_PRUI08_1(request):
    return render_to_response('profesor/reportes/PRUI08.1.html',context_instance=RequestContext(request))

def profesor_reportes_PRUI08_2(request):
    return render_to_response('profesor/reportes/PRUI08.2.html',context_instance=RequestContext(request))

def profesor_calendario(request):
    return render_to_response('profesor/calendario.html',context_instance=RequestContext(request))

def profesor_tutorias(request):
    return render_to_response('profesor/tutorias.html',context_instance=RequestContext(request))

def profesor_ingresa_calificacion(request):
    return render_to_response('profesor/IngresaCalificacion.html',context_instance=RequestContext(request))

def perfiles_profesor(request):
    return render_to_response('perfiles/maldonadoCastilloIdalia.html',context_instance=RequestContext(request))

def perfiles_materia(request):
    return render_to_response('perfiles/ingenieria-de-software.html',context_instance=RequestContext(request))

def perfiles_grupo(request):
    return render_to_response('perfiles/3CM5.html',context_instance=RequestContext(request))   

def profesor_tutorias_comentar(request):
    return render_to_response('profesor/comentar-tutoria.html',context_instance=RequestContext(request))
