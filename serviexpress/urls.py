from django.urls import path
from .views import lista_prueba, guardar_prueba, eliminar_prueba

urlpatterns = [
    path('', lista_prueba),
    path('nueva_prueba/', guardar_prueba, name='nueva_prueba'),
    path('eliminar_prueba/<int:prueba_id>/', eliminar_prueba, name='eliminar_prueba')
]
