from django.http import JsonResponse
from .models import Tarefa
from django.utils import timezone

# São os filtros do banco, assim como os selects

def listar_tarefa(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas) , safe=False)

def abertas(request):
    tarefa_aberta = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefa_aberta) , safe=False)

def urgente(request):
    tarefa_urgente = Tarefa.objects.filter(prioridade='URGENTE').values()
    return JsonResponse(list(tarefa_urgente) , safe=False)

def nao_urgente(request):
    tarefa_nao_urgente = Tarefa.objects.filter(prioridade='NAO_URGENTE').values()
    return JsonResponse(list(tarefa_nao_urgente) , safe=False)

def aberta_urgente(request):
    abertaeurgente = Tarefa.objects.filter(status='ABERTA' , prioridade='URGENTE').values()
    return JsonResponse(list(abertaeurgente) , safe=False)

def busca_id(request, id):
    tarefa_id = Tarefa.objects.filter(id= id).values()
    return JsonResponse(list(tarefa_id) , safe=False)

def atrasada(request):

    hoje = timezone.now().date()

    tarefa_atrasada = Tarefa.objects.filter(data_entrega__lt=hoje , status = 'ABERTA'  ).values()
    return JsonResponse(list(tarefa_atrasada) , safe=False)

def busca_titulo(request, titulo): 
    tarefa_titulo = Tarefa.objects.filter(titulo__iexact=titulo).values()
    return JsonResponse(list(tarefa_titulo), safe=False)

