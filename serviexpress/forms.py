from django import forms
from .models import Cliente
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

class clienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username','password','rut','nombre',
        'apellido','telefono']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class loginForm(AuthenticationForm):
    class Meta:
        model = Cliente
        fields = ['username','password']
    
