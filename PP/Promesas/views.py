from django.shortcuts import render


from Promesas.models import Candidato
from Promesas.models import Promesa

from django.utils import timezone

from Promesas.forms import *

def index(request):
    candidatos_list = Candidato.objects.all()
    context = {'candidatos_actual_list': candidatos_list}
    return render(request, 'Promesas/index.html', context)

def perfil(request,candidato_id):
	candidato_single = Candidato.objects.get(id = candidato_id)
	if request.method == 'POST':
		form = PromesaForm(request.POST)
		candidato_single.promesas.create(informante = request.POST['informante'] , fuente = request.POST['fuente'] , fecha = timezone.now() , lugar = request.POST['lugar'], descripcion = request.POST['descripcion'])

	promesas_list = candidato_single.promesas.all()
	context = {'candidato': candidato_single , 'promesas': promesas_list}
	return render(request, 'Promesas/perfil.html', context)
