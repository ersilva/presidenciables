from django.db import models
import datetime
from django.utils import timezone
from django.conf.locale import tr

class Partido(models.Model):
	nombre = models.CharField(max_length=50)	
	logo = models.CharField(max_length=100, blank=True)
	info = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return self.nombre

class Pacto(models.Model):
	nombre = models.CharField(max_length=50)
	logo = models.CharField(max_length=100, blank=True)
	info = models.CharField(max_length=100, blank=True)
	
class Candidato(models.Model):
	partido = models.ForeignKey(Partido, related_name = "candidatos")
	pacto = models.ForeignKey(Pacto, related_name = "candidato", blank=True, null=True)
	nombre = models.CharField(max_length=100)
	info = models.CharField(max_length=100, blank=True)
	foto = models.CharField(max_length=200, blank=True)
	def __unicode__(self):
		return self.nombre
	
class Promesa(models.Model):
	candidato = models.ForeignKey(Candidato, related_name = "promesas")
	informante = models.CharField(max_length=100)
	fuente = models.CharField(max_length=200, blank=True)
	fecha = models.DateTimeField('date published')
	lugar = models.CharField(max_length=100, blank=True)
	descripcion = models.CharField(max_length=500)
	##nombre = models.CharField(max_length=100)
	
	def __unicode__(self):
		##return self.nombre 
		return "De " + self.candidato.nombre + " por " + self.informante
	
	def publicada_recientemente(self):
		return self.fecha >= timezone.now() - datetime.timedelta(days=30)
		publicada_recientemente.admin_order_field = 'fecha'
		publicada_recientemente.boolean = True
		publicada_recientemente.short_description = 'Promesas del ultimo mes'
