from django.shortcuts import render

from Promesas.models import Candidato
from Promesas.models import Promesa

from django.utils import timezone

def index(request):
    candidatos_list = Candidato.objects.all()
    context = {'candidatos_actual_list': candidatos_list}
    return render(request, 'Promesas/index.html', context)

def perfil(request,candidato_id):
	candidato_single = Candidato.objects.get(id = candidato_id)
	context = {'candidato': candidato_single}
	return render(request, 'Promesas/perfil.html', context)
