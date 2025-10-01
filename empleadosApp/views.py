from django.shortcuts import render
from empleadosApp.models import Empleado
#importar el formulario
from empleadosApp.form import EmpleadoRegistroForm

# Redireccionar a donde queramos
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your views here.
def empleadoData(request):
    empleados = Empleado.objects.all()
    data = {'empleados':empleados}
    return render(request, 'empleadosApp/empleados.html' , data)

def crearEmpleado(request):
    form = EmpleadoRegistroForm()
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmpleadoRegistroForm() # limpiar formulario
            return HttpResponseRedirect(reverse('listaEmpleado')) # IR a la lista de empleados

    data = {'form':form,
            'titulo':'Crear Empleado 👨',
            'txtBoton' : 'Crear Empleado',
            'colorAlert': 'alert-danger'
            }
    return render(request,'empleadosApp/empleadoRegistro.html',data)

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    form = EmpleadoRegistroForm(instance=empleado)
    if request.method == 'POST':
        form = EmpleadoRegistroForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listaEmpleado')) # IR a la lista de empleados

    data = {'form':form,
            'titulo':'Editar Empleado 👨',
            'txtBoton' : 'Guardar cambios',
            'colorAlert': 'alert-warning'
            }
    return render(request,'empleadosApp/empleadoRegistro.html',data)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    return HttpResponseRedirect(reverse('listaEmpleado'))

