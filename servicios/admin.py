from django.contrib import admin
from .models import Servicio  # importando el servicio


# Aqui se registrara los modelos creados en el archivo 'admin.py' para poder verlos en el panel de administracion de la pagina

# Esta clase es para poder mostrar los campos de cracion y actualizado de la tabla
class Servicio_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Con esto se hace que los campos sean de solo lectura en la vista


admin.site.register(Servicio, Servicio_admin)  # Muestra en la vista la app 'servicio'
