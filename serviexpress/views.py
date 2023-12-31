from django.shortcuts import render, redirect
from .models import Cliente, Empleado, ReservaHora
from .forms import clienteForm, loginForm, reservaHoraForm, servicioForm, proveedorForm, pedidosForm, modificarReservaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Acesso a las paginas

@login_required
def homepage(request):
    context = {}
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
    
#Login de cliente/empleado
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
                    print(username)
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

#Cerrar sesion 
def signout(request):
    logout(request)
    return redirect('menu')

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
@login_required
def list_reservas(request):
    reservas = ReservaHora.objects.all()
    print(reservas)
    return render(request, 'serviexpress/listaReserva.html', {'reservas': reservas})

#Modificar Reservas de hora
@login_required
def mod_reservas(request, id):
    reservas = ReservaHora.objects.get(id=id)
    print('ERROR 1')
    if request.method == 'POST':
        print('ERROR 4')
        form = modificarReservaForm(request.POST, instance=reservas)
        print('ERROR 2')
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('ERROR 4')

    print('ERROR 3')
    return render(request, 'serviexpress/listaReserva.html', {'form':form})


#Registro de Servicios
@login_required
def registroServicio(request):
    if request.method == "POST":
        print(request.POST)
        form = servicioForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            print("Registro guardado exitosamente")
            return redirect('empleado')
        else:
            print("Formulario no válido. Errores:", form.errors)
            return redirect('servicio')
    else:
        form = servicioForm
        
    return render(request, 'serviexpress/registroServicio.html', {'form':form})

#Registro de proveedores
@login_required
def registroProveedores(request):
    if request.method == "POST":
        print(request.POST)
        form = proveedorForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            print("Proveedor guardado exitosamente")
            return redirect('empleado')
        else:
            print("Formulario no válido. Errores:", form.errors)
            return redirect('proveedor')
    else:
        form = servicioForm
        
    return render(request, 'serviexpress/registroProveedor.html', {'form':form})

#Registro de pedidos
@login_required
def registroPedido(request):
    if request.method == "POST":
        print(request.POST)
        form = pedidosForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            print("Proveedor guardado exitosamente")
            return redirect('empleado')
        else:
            print("Formulario no válido. Errores:", form.errors)
            return redirect('pedido')
    else:
        form = servicioForm
        
    return render(request, 'serviexpress/registroPedido.html', {'form':form})