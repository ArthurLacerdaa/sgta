from django.urls import path
from .views import listar_tarefa
from .views import abertas

urlpatterns = [
    path('tarefas/' , listar_tarefa),
    path('tarefas/abertas' , abertas)
]

