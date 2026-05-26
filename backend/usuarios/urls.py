from django.urls import path
<<<<<<< HEAD
from .views import listar_usuarios, buscar_usuario_por_id

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/<int:id>/', buscar_usuario_por_id),
=======
from .views import listar_usuario, buscar_usuario_por_id

urlpatterns = [
    path('usuarios/' , listar_usuario),
    path('usuarios/id/<int:id>/' , buscar_usuario_por_id),
>>>>>>> 6963cd2023785647491a85d84e7e9d5d6e64e2f1
]