from django.forms import ModelForm
from Promesas.models import Promesa


class PromesaForm(ModelForm):
	class Meta:
		model = Promesa
		fields = ['informante','fuente','fecha','lugar','descripcion']
