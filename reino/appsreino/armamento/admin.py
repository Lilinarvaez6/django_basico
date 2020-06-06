# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from appsreino.armamento.models import Armamento
from appsreino.armamento.models import Habilidad

admin.site.register(Armamento)
admin.site.register(Habilidad)

