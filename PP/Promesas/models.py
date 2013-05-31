from django.db import models

class Partido(models.Model):
	nombre = models.CharField(max_length=50)	
	logo = models.CharField(max_length=100)
	info = models.CharField(max_length=100)

class Candidato(models.Model):
	partido = models.ForeignKey(Partido, related_name = "candidatos")
	nombre = models.CharField(max_length=100)
	info = models.CharField(max_length=100)
	
class Promesa(models.Model):
	candidato = models.ForeignKey(Candidato, related_name = "promesas")
	informante = models.CharField(max_length=100)
	fuente = models.CharField(max_length=200)
	fecha = models.DateTimeField('date published')
	lugar = models.CharField(max_length=100)

