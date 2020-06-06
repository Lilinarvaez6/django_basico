from appsreino.soldado.views import index,CrearSoldado,tipos,armas,listar_views,EditarSoldado,HistorialSoldado
from django.conf.urls import url

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^form/', CrearSoldado.as_view(), name='soldado_crear'),
	url(r'^ajax_tipo/', tipos, name='ajax_tipo'),
	url(r'^ajax_armas/', armas, name='ajax_armas'),
	url(r'^listar/', listar_views.as_view(), name='listar'),
	url(r'^editar/(?P<pk>\d+)/$', EditarSoldado.as_view(), name='editar'),
	url(r'^historial/(?P<pk>\d+)/$', HistorialSoldado.as_view(), name='historial'),	
]






