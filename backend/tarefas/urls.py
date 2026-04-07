from django.urls import path
from .views import listar_tarefa
from .views import abertas
from .views import urgente
from .views import nao_urgente
from .views import aberta_urgente
from .views import busca_id
from .views import atrasada
from .views import busca_titulo

# É como vamos acessar e vizualiar as views

urlpatterns = [
    path('tarefas/' , listar_tarefa),
    path('tarefas/abertas' , abertas),
    path('tarefas/prioridade/urgentes/' , urgente),
    path('tarefas/prioridade/nao_urgentes/' , nao_urgente),
    path('tarefas/abertas/urgentes' , aberta_urgente),
    path('tarefas/<int:id>' , busca_id),
    path('tarefas/atrasadas' , atrasada),
    path('tarefas/busca/<str:titulo>/', busca_titulo)

]

