from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import User, Jefe, Empleado, FamiliaVehiculo, Equipo, Estado, OrdenTrabajo, EstadoRep, Aprobacion, Reparacion

admin.site.register(User)
admin.site.register(Jefe)
admin.site.register(Empleado)
admin.site.register(FamiliaVehiculo)
admin.site.register(Equipo)
admin.site.register(Estado)
admin.site.register(OrdenTrabajo)
admin.site.register(EstadoRep)
admin.site.register(Aprobacion)
admin.site.register(Reparacion)