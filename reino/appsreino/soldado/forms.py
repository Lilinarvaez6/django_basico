from django import forms
from appsreino.soldado.models import Soldado,Tipo, BaseConocimiento
from appsreino.armamento.models import Armamento, Habilidad, Tipo

#contiene el modelo soldaddo para utilizarlo en el formulario
class SoldadoForm(forms.ModelForm):	
	class Meta:
		model = Soldado
		fields = ['nombre','estado']
		exclude = ['armamento']
		label = {
		'nombre': 'Nombre',
		'estado': 'Estado',
		}
		widgets ={
		'nombre' :forms.TextInput(attrs = { 'class': 'form-control' }),
		'estado' :forms.Select(attrs = { 'class': 'form-control'}),
		}
#contiene el modelo Armamento para utilizarlo en el formulario		
class ArmamentoForm(forms.ModelForm):	
	class Meta:
		model = Armamento
		fields = ['nombreA','tipoA','puntajeDannoA','habilidadA']
		label ={
		'nombreA' :'Nombre Armamento',
		'habilidadA' : 'Habilidad',
		'tipoA' : 'tipo Armamento',
		}
		widgets = {
		'habilidadA' :forms.Select(attrs = { 'class': 'form-control'}),
		}
	#por defecto deja vacio el campo tipoA, nombreA
	def __init__(self, *args, **kwargs):
		super(ArmamentoForm, self).__init__(*args, **kwargs)
		self.fields['tipoA'] = forms.ModelChoiceField(queryset=Tipo.objects.none(),widget =  forms.Select(attrs = {'class':'form-control'})) 
		self.fields['nombreA'] = forms.ModelChoiceField(queryset=Armamento.objects.none(),widget =  forms.Select(attrs = {'class':'form-control'})) 

#contiene el modelo BaseConocimiento para guardar el historial despues una actualizacion		
class BaseConocimientoForm(forms.ModelForm):	
	class Meta:
		model = BaseConocimiento
		fields = '__all__'