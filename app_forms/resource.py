from import_export import resources  
from .models import OrdenTrabajo, Equipo, Empleado
    
class OrdenTrabajoResource(resources.ModelResource):  
    class Meta:  
        model = OrdenTrabajo

class EquipoResource(resources.ModelResource):  
    class Meta:  
        model = Equipo

class EmpleadoResource(resources.ModelResource):  
    class Meta:  
        model = Empleado