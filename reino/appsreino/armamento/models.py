# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#modelo para los tipos de armamentos
#ejemplo: cuerpo, media, larga
#retorna el nombre del tipo
class Tipo (models.Model):
	nombreT = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombreT

#modelo de las habilidades 
#ejemplo: volar, luchar 
#retorna el nombre de la habilidad
class Habilidad (models.Model):
	nombreH = models.CharField(max_length = 100)
	def __str__(self):
		return self.nombreH

#modelo del armamento 
#contiene: el nombre, puntaje del armamento, habilidad y tipo de armamento con el que se puede usar
#retorna el nombre del Armamento
class Armamento (models.Model):
	nombreA = models.CharField(max_length=100)
	tipoA =  models.ForeignKey(Tipo,null = True, blank= True, on_delete=models.CASCADE)
	puntajeDannoA = models.IntegerField(default=0)
	habilidadA  = models.ForeignKey(Habilidad,null = True, blank= True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombreA

