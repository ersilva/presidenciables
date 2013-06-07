from django.db import models
import datetime
from django.utils import timezone

class Partido(models.Model):
	nombre = models.CharField(max_length=50)	
	logo = models.CharField(max_length=100)
	info = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Candidato(models.Model):
	partido = models.ForeignKey(Partido, related_name = "candidatos")
	nombre = models.CharField(max_length=100)
	info = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre
	
class Promesa(models.Model):
	candidato = models.ForeignKey(Candidato, related_name = "promesas")
	informante = models.CharField(max_length=100)
	fuente = models.CharField(max_length=200)
	fecha = models.DateTimeField('date published')
	lugar = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	##nombre = models.CharField(max_length=100)
	
	def __unicode__(self):
		##return self.nombre 
		return self.candidato.nombre, "-", self.lugar
	
	def publicada_recientemente(self):
		return self.fecha >= timezone.now() - datetime.timedelta(days=30)
		publicada_recientemente.admin_order_field = 'fecha'
		publicada_recientemente.boolean = True
		publicada_recientemente.short_description = 'Promesas del ultimo mes'
