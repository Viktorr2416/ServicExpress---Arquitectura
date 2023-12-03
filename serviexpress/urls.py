from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage,name="home"),
    path('registro/',views.registroCliente, name='registro'),
    path('menu/',views.menu, name='menu'),
    path('empleado/',views.homeE, name='empleado'),
    path('registrar/',views.registrar_cliente, name='registrar'),
    path('login/', views.loginCliente, name='login'),
    path('logeo/', views.login_cliente, name='logeo_cliente')
]
