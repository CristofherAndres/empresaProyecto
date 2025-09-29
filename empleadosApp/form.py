from django import forms

class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    rut = forms.CharField(max_length=15)
    correo = forms.CharField(max_length=150)
    telefono = forms.CharField(max_length=12)