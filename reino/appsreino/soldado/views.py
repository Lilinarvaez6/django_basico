# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from appsreino.soldado.forms import SoldadoForm, ArmamentoForm,BaseConocimientoForm
from appsreino.armamento.models import Armamento,Habilidad,Tipo
from appsreino.soldado.models import Soldado,BaseConocimiento
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy

#crea un soldado 
class CrearSoldado(CreateView):
	model= Soldado
	template_name = 'soldado/soldado_form.html'
	form_class = SoldadoForm
	second_form_class = ArmamentoForm
	third_form_class = BaseConocimientoForm
	success_url = reverse_lazy('listar')

	def get_context_data(self, **kwargs):
		context = super(CrearSoldado, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		#captura el armamento seleccionado al enviar el formulario 
		arm = request.POST.get('nombreA');	
		#trae el modelo del armamento seleccionado 
		armas = Armamento.objects.get(id=arm)
		form3 = self.third_form_class(request.POST)
		#validad  el formulario
		if form.is_valid():
			#guardar el soldado con su armamento
			soldado = form.save(commit=False)
			soldado.armamento = armas
			soldado.save()
			#guardar en el historial del soldado
			conocimiento = form3.save(commit=False)
			conocimiento.Soldado = soldado
			conocimiento.armamento = armas			
			conocimiento.save()
			return HttpResponseRedirect(self.get_success_url())
		else :
			return self.render_to_response(self.get_context_data(form= form))

#lista todos los soldados con su informacion y template correspondiente
class listar_views(ListView):
	model = Soldado
	template_name = "soldado/listar.html"

#lista todo el historial del soldado con su informacion y template correspondiente
class HistorialSoldado(ListView):
	model = BaseConocimiento
	second_model= Soldado
	third_model= Armamento
	template_name = "soldado/historial.html"
	form_class = BaseConocimientoForm
	second_form_class = SoldadoForm
	third_form_class = ArmamentoForm
	def get_context_data(self, **kwargs):
		#toma el pk y busca en la Baseconocimiento toda la informacion
		#para retornarlo en el template y listarlo
		context = super(HistorialSoldado, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)		
		soldado = self.second_model.objects.get(id = pk)
		armamento = self.third_model.objects.filter(baseconocimiento__Soldado_id = pk)
		if 'form' not in context:
			context['form'] = soldado
		if 'form2' not in context:
			context['form2'] = armamento
		return context
	def post(self, request, **kwargs):
		self.object = self.get_object
		form = self.second_form_class(request.POST)
		return self.render_to_response(self.get_context_data(form= form))

#edita el soldado seleccionado con su informacion y template correspondiente
class EditarSoldado(UpdateView):
	model= Soldado
	second_model= Armamento
	template_name = 'soldado/soldado_form.html'
	form_class = SoldadoForm
	second_form_class = ArmamentoForm
	third_form_class = BaseConocimientoForm
	success_url = reverse_lazy('listar')

	def get_context_data(self, **kwargs):
		#toma el pk y busca su informacion para editarlo en el template del form
		context = super(EditarSoldado, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		soldado = self.model.objects.get(id = pk)
		armamento = self.second_model.objects.get(id = soldado.armamento_id)
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance = armamento)
		return context

	def post(self, request,*args, **kwargs):
		self.object = self.get_object
		id_soldado = kwargs['pk']
		soldad = self.model.objects.get(id = id_soldado)	
		arm = request.POST.get('nombreA');
		armas = Armamento.objects.get(id=arm)
		form = self.form_class(request.POST, instance = soldad)
		form3 = self.third_form_class(request.POST)
		#validad  el formulario
		if form.is_valid():
			#guardar el soldado con su armamento
			soldado = form.save(commit=False)			
			soldado.armamento = armas
			soldado.save()
			#guardar en el historial del soldado
			conocimiento = form3.save(commit=False)
			conocimiento.Soldado = soldad
			conocimiento.armamento = armas			
			conocimiento.save()

			return HttpResponseRedirect(self.get_success_url())
		else :
			return self.render_to_response(self.get_context_data(form= form))

#muestra el template de inicio
def index(request):
	return render(request, 'soldado/index.html')

#muestra el template de las opciones posibles de los tipos dado la habilidad 
#captura el id_habilidad para buscarlos
def tipos(request):
	id_habilidades= request.POST.get('id_habilidad');
	tipoarmamento = Tipo.objects.filter(armamento__habilidadA_id=id_habilidades).distinct('id').values('id','nombreT')
	return render(request, 'soldado/tipos.html',{'tipos' : tipoarmamento})

#muestra el template de las opciones posibles de los armas dado la habilidad y tipo
#captura el id_habilidad y id_tipo
def armas(request):
	id_habilidades= request.POST.get('id_habilidades');
	id_tipos= request.POST.get('id_tipos');
	armass = Armamento.objects.filter(habilidadA_id=id_habilidades).filter(tipoA = id_tipos).distinct('id').values('id','nombreA','puntajeDannoA')
	return render(request, 'soldado/armas.html',{'armas' : armass})