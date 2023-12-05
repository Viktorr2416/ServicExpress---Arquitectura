from django.shortcuts import render, redirect
from .models import Cliente, Empleado, ReservaHora
from .forms import clienteForm, loginForm, reservaHoraForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Acesso a las paginas

@login_required
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

@login_required
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
            user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password"])
            user.save()
            print("Cliente guardado")
            print("Usuario guardado")
            return redirect('login_cliente')
        else:
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = clienteForm
        
    return render(request, 'serviexpress/registro.html',{'form':form})
    
#Registro de cliente
def login_cliente(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username,password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '¡Inicio de sesión exitoso!')
                try:
                    # Intentar buscar en Cliente
                    cliente = Cliente.objects.get(username=username)
                    # Redirigir a una página específica para clientes
                    return redirect('home')  # Cambia 'ruta_para_cliente' por la URL o nombre de ruta real
                except Cliente.DoesNotExist:
                    # Si no se encuentra en Cliente, buscar en Empleado
                    try:
                        empleado = Empleado.objects.get(correo=username)  # Asumiendo que 'correo' es el campo de identificación
                        # Redirigir a una página específica para empleados
                        return redirect('empleado')  # Cambia 'ruta_para_empleado' por la URL o nombre de ruta real
                    except Empleado.DoesNotExist:
                        # Si no se encuentra en ninguno de los dos
                        messages.error(request, 'Usuario no encontrado en Clientes o Empleados.')
                
            else:
                print(user)
                messages.error(request, 'ERROR FASE 2: Credenciales inválidas.')
        else:
            messages.error(request, 'ERROR FASE 1: Formulario no válido.')

    else:
        form = loginForm()

    return render(request, 'serviexpress/login.html', {'form': form})


#Registro Reserva de hora
@login_required
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
        
    return render(request, 'serviexpress/reservaHora.html', {'form':form})

#Listar Reservas de hora
def list_reservas(request):
    reservas = ReservaHora.objects.all()
    print(reservas)
    return render(request, 'serviexpress/listaReserva.html', {'reservas': reservas})
