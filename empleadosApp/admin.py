from django.contrib import admin

from empleadosApp.models import Empleado

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido']

admin.site.register(Empleado, EmpleadoAdmin)
