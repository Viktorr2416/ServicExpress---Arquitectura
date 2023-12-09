from django import forms
from datetime import date
from .models import Cliente, ReservaHora, Servicio, Proveedor, OrdenPedido
from .widgets import formato_hora
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

class clienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username','password','rut','nombre',
        'apellido','telefono']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class loginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', max_length=64)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Aquí puedes agregar validaciones adicionales si lo necesitas

        return cleaned_data
    
class reservaHoraForm(ModelForm):
    class Meta:
        model = ReservaHora
        fields = ['hora','fecha','servicio']
    
    hora = forms.TimeField(widget=formato_hora)
    
    def clean_hora(self):
        hora = self.cleaned_data.get('hora')

        if hora:
            if not (6 <= hora.hour < 20):
                raise ValidationError('La hora de reserve debe ser entre 6 A.M y 8 P.M')
            
        return hora
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        if fecha:
            today = date.today()
            if fecha < today:
                raise ValidationError('La fecha de reserva no puede ser anterior a la fecha actual')
            
        return fecha
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class modificarReservaForm(ModelForm):
    class Meta:
        model = ReservaHora
        fields = ['hora','fecha','servicio']

class servicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre','precio']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class proveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nom_empresa','contacto', 'rubro']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
        
class pedidosForm(ModelForm):
    class Meta:
        model = OrdenPedido
        fields = ['fecha_solicitud','nom_producto', 'descripcion', 'cant_produc']
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha_solicitud')

        if fecha:
            today = date.today()
            if fecha < today:
                raise ValidationError('La fecha de solicitud no puede ser anterior a la fecha actual')
            
        return fecha
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)