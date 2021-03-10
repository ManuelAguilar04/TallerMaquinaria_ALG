from django.db import models
from django.utils.translation import ugettext as _

class User(models.Model):
    username = models.CharField('Usuario',max_length=30)
    password = models.CharField('Contraseña',max_length=30)

    def __str__(self):
        return self.username

class Jefe(models.Model):
    codJefe = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)    

    def __str__(self):
        return f' {self.nombre} {self.apellido}'
    
    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
        )

class Empleado(models.Model):
    codEmpleado = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    jefe = models.ForeignKey(Jefe,on_delete=models.CASCADE, null=True)    

    def __str__(self):
        return f' {self.codEmpleado} {self.nombres} {self.apellidos}' 

    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
            ('is_coordinador',_('Is Coordinador')),
        )

class FamiliaVehiculo(models.Model):
    descripcionFamilia = models.CharField('Descripción familia',max_length=50, null=False)

    def __str__(self):
        return self.descripcionFamilia

    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
            ('is_coordinador',_('Is Coordinador')),
        )

class Equipo(models.Model):
    codEquipo = models.CharField('Código de Equipo',max_length=10, primary_key=True)
    descripcionEqui = models.CharField('Descripción de Equipo',max_length=50,null=False)
    codFamilia = models.ForeignKey(FamiliaVehiculo, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.codEquipo

    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
            ('is_coordinador',_('Is Coordinador')),
        )

class Estado(models.Model):
    descEstado = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.descEstado
    
    class Meta:
        verbose_name_plural = 'Estados'
        
class OrdenTrabajo(models.Model):
    codOrdenTrab = models.CharField('Código de orden',max_length=10 ,primary_key=True)
    descOrden = models.CharField('Descripción',max_length=50, null=True)
    codEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.codOrdenTrab

    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
            ('is_coordinador',_('Is Coordinador')),
        )

class EstadoRep(models.Model):
    descRep = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.descRep

    class Meta:
        verbose_name_plural = 'Estado de reparción'

class Aprobacion(models.Model):
    estadoApro = models.CharField(max_length=50)
    
    def __str__(self):
        return self.estadoApro

    class Meta:
        verbose_name_plural = 'Aprobaciones'
    

class Reparacion(models.Model):
    descripActi = models.CharField('Descripción de la actividad', max_length=50, null=True)
    fecha = models.DateField('Fecha',auto_now_add=True)
    horaIni = models.TimeField('Hora de inicio', auto_now_add=True)
    horaFin = models.TimeField('Hora de finalización')
    jefe = models.ForeignKey(Jefe, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    codequipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    ordenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    estadoReparacion = models.ForeignKey(EstadoRep, on_delete=models.CASCADE)
    estadoApro = models.ForeignKey(Aprobacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripActi
    
    class Meta:
        permissions = (
            ('is_jefe',_('Is Jefe')),
            ('is_coordinador',_('Is Coordinador')),
            ('is_empleado',('Is Empleado'))
        )

