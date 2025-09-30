from django import forms
from empleadosApp.models import Empleado

# Sirve para actualizar
class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=15)
    correo = forms.CharField(max_length=150)
    telefono = forms.CharField(max_length=12)

# Este form sirve para insertar
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'