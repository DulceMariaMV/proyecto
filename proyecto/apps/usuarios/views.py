#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def inicio_view(request):
	return render_to_response("inicio.html",{},context_instance=RequestContext(request))


def registro(request):
	if request.method=="POST":
		form_usuario=UserCreationForm(request.POST)
		if form_usuario.is_valid():
			form_usuario.save()
			usuario=request.POST["username"]
			#buscando al usuario qe emos creado
			nuevo_usuario=User.objects.get(username=usuario)
			nuevo_usuario.save()
			#creamos su perfil
			perfil=perfil_usuario.objects.create(user=nuevo_usuario)
			perfil.save()
			#return HttpResponse("registrado")
			return render_to_response("usuarios/perfil.html")
	else:
		form_usuario=UserCreationForm()	
	return render_to_response("registro.html",{'formulario':form_usuario},context_instance=RequestContext(request))	

def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return render_to_response("usuarios/perfil.html")
	form=AuthenticationForm()
	return render_to_response("usuarios/login.html",{"form":form},RequestContext(request))

def perfil(request):
	#return HttpResponse("registrado")
	return render_to_response("usuario/perfil.html",{"nombre":request.session["name"]},RequestContext(request))	


def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/plantillas/")
