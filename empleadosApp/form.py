from django import forms
from empleadosApp.models import Empleado

#VAlidar datos
from django.core import validators

# Sirve para actualizar
class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    rut = forms.CharField()
    correo = forms.CharField()
    telefono = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'

# Este form sirve para insertar
class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10)
    ])
    apellido = forms.CharField()
    rut = forms.CharField()
    correo = forms.CharField()
    telefono = forms.CharField(required=False)

    def clean_correo(self):
        inputCorreo = self.cleaned_data['correo']
        if inputCorreo.find('@') == -1 :
            raise forms.ValidationError("El correo debe tener un @")
        if len(inputCorreo) < 5:
            raise forms.ValidationError("Debes tener mas de 5 caracteres")
        return inputCorreo

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'