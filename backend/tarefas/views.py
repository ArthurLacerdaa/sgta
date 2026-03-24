from django.http import JsonResponse
from .models import Tarefa

def listar_tarefa(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas) , safe=False)

def abertas(request):
    tarefa_aberta = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefa_aberta) , safe=False)