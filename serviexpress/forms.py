from django import forms
from .models import Cliente, ReservaHora
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

class clienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username','password','rut','nombre',
        'apellido','telefono']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

##class loginForm(AuthenticationForm):
    ##class Meta:
        ##model = Cliente
        ##fields = ['username','password']

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)