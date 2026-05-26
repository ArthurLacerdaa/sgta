from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tarefas.urls')),
<<<<<<< HEAD
    path('api/', include('usuarios.urls')),
]
=======
    path('api/', include('usuarios.urls'))

]
>>>>>>> 6963cd2023785647491a85d84e7e9d5d6e64e2f1
