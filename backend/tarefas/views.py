from django.http import JsonResponse
from .models import Tarefa
from django.utils import timezone

def listar_tarefa(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas) , safe=False)


def tarefas_por_status_prioridade(request, status, prioridade):
    tarefas = Tarefa.objects.filter(status=status)

    if prioridade:
        tarefas = tarefas.filter(prioridade=prioridade)
    
    data = list(tarefas.values())
    return JsonResponse(data, safe=False)


def tarefa_por_id(request, id):
    tarefa = Tarefa.objects.filter(id=id).values().first()

    if tarefa:
        return JsonResponse(tarefa)
    return JsonResponse({'erro': 'Tarefa nao encontrada'})
    

def atrasada(request):

    hoje = timezone.now().date()

    tarefa_atrasada = Tarefa.objects.filter(data_entrega__lt = hoje, status = 'ABERTA').values()
    return JsonResponse(list(tarefa_atrasada), safe=False)


def buscar_titulo(request, titulo):
    tarefa_titulo = Tarefa.objects.filter(titulo__iexact = titulo).values()
    return JsonResponse(list(tarefa_titulo), safe=False)