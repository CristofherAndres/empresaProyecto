from django.shortcuts import render
from empleadosApp.models import Empleado
#importar el formulario
from empleadosApp.form import EmpleadoRegistroForm


# Create your views here.
def empleadoData(request):
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render(request, 'empleadosApp/empleados.html' , data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()
    data = {'form':form}
    return render(request,'empleadosApp/empleadoRegistro.html',data)

