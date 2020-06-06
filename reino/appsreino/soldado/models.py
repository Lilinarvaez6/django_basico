# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from appsreino.armamento.models import Armamento

#modelo para los tipos de estados del soldados
#ejemplo: bien, enfermo, muerto
#retorna el nombre del tipo
class Tipo(models.Model):
	nombre = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombre	

#modelo para los soldados
#contiene: el nombre, estado y armamento del soldado
class Soldado(models.Model):
	nombre = models.CharField(max_length = 100 ,null = True)
	estado = models.ForeignKey(Tipo, null = True, blank= True, on_delete=models.CASCADE)
	armamento = models.ForeignKey(Armamento,null = True, blank= True, on_delete=models.CASCADE)

#modelo para el historial de los soldados
#contiene: armamento, soldado	
class BaseConocimiento(models.Model):
	armamento = models.ForeignKey(Armamento,null = True, blank= True, on_delete=models.CASCADE)
	Soldado = models.ForeignKey(Soldado, null = True, blank= True, on_delete=models.CASCADE)