from django.shortcuts import render, redirect
from .models import prueba
from .forms import clienteForm, loginForm, reservaHoraForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Acesso a las paginas

def homepage(request):
    context={}
    return render(request, 'serviexpress/home.html', context)

def registroCliente(request):
    context={}
    return render(request, 'serviexpress/registro.html', context)

def loginCliente(request):
    context={}
    return render(request, 'serviexpress/login.html', context)

def menu(request):
    context={}
    return render(request, 'serviexpress/menu.html', context)

def homeE(request):
    context={}
    return render(request, 'serviexpress/homeE.html', context)

# Fin de accesos 

# Funciones 

#Registro de clientes
def registrar_cliente(request):
    if request.method == "POST":
        print(request.POST)
        form = clienteForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            print("Cliente guardado")
            return redirect('login')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = clienteForm
        
    return render(request, 'serviexpress/registro.html',{'form':form})
            

#Login de empleados
def login_cliente(request):
    
    print(request.POST)
    if request.method == 'POST':
        form = loginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verificar las credenciales del usuario
            print("Correo:", username)
            print("password", password)
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            
            if user is not None:
                login(request, user)
                messages.success(request, '¡Inicio de sesión exitoso!')
                return redirect('home')
            else:
                messages.error(request, 'ERROR FASE 2.')
        else:
            messages.error(request, 'ERROR FASE 1.')

    return redirect('login')

#Registro Reserva de hora
def reservaHora(request):
    if request.method == "POST":
        print(request.POST)
        form = reservaHoraForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            print("Reserva guardada exitosamente")
            return redirect('home')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = reservaHoraForm
        
    return render(request, 'home', {'form':form})