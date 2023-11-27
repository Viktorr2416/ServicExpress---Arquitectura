from django.shortcuts import render, redirect
from .models import prueba

# Create your views here.
def lista_prueba(request):
    listar = prueba.objects.all()
    print(listar)
    return render(request, 'lista_prueba.html', {'listar':listar})

def guardar_prueba(request):
    Enviodatos = prueba(titulo=request.POST['Titulo'], descripcion=request.POST['Descripcion'])
    Enviodatos.save()
    return redirect('/lista/')

def eliminar_prueba(request, prueba_id):
    eliminar = prueba.objects.get(id=prueba_id)
    print(prueba_id)
    eliminar.delete()
    return redirect('/lista/')
    
    