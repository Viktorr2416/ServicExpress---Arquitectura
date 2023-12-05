from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('login/', views.login_cliente, name='login_cliente'),
    path('home/',views.homepage,name="home"),
    path('empleado/',views.homeE, name='empleado'),
    path('registrar/',views.registrar_cliente, name='registrar'),
    path('reserva-hora/', views.reservaHora, name='reserva'),
    path('lista-reserva/', views.list_reservas, name='listar_reserva' )
]
