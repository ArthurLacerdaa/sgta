from django.urls import path
from .views import listar_tarefa, tarefas_por_status_prioridade, tarefa_por_id, atrasada , buscar_titulo

urlpatterns = [
    path('tarefas/' , listar_tarefa),
    path('tarefas/filtro/<str:status>/<str:prioridade>/', tarefas_por_status_prioridade),
    path('tarefas/id/<int:id>/' , tarefa_por_id),
    path('tarefas/busca/<str:titulo>/', buscar_titulo),
    path('tarefas/atrasadas/', atrasada)
]