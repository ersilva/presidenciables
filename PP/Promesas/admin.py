from django.contrib import admin

from Promesas.models import Promesa
from Promesas.models import Candidato
from Promesas.models import Partido
from Promesas.models import Pacto

class PromesaAdmin(admin.ModelAdmin):
	fieldsets = [
	('Candidato', {'fields': ['candidato']}),
	('Que prometio?', {'fields': ['descripcion']}),
	##('Que prometio?', {'fields': ['nombre','descripcion']}),
	('En que momento?', {'fields': ['fecha']}),
	('Fuentes', {'fields': ['informante', 'fuente','lugar']}),
	]
	
	list_display = ('descripcion', 'candidato', 'fecha', 'publicada_recientemente')
	list_filter = ['fecha']
	search_fields = ['candidato']

admin.site.register(Partido)
admin.site.register(Pacto)
admin.site.register(Candidato)
admin.site.register(Promesa, PromesaAdmin)
