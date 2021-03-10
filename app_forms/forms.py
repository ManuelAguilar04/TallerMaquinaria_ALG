from django.forms import ModelForm
from django import forms
from datetime import datetime, date, time
from .models import Reparacion, User, Empleado, Jefe, Equipo, OrdenTrabajo, FamiliaVehiculo


class ReparacionForm(ModelForm):
    class Meta  :
        model = Reparacion
        fields = '__all__'
        widgets = {
            'descripActi': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class' : 'form-control'}),
            'horaIni': forms.TimeInput(attrs={'class': 'form-control'}),
            'horaFin': forms.TimeInput(attrs={'class': 'form-control'}),
            'jefe': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'codequipo': forms.Select(attrs={'class': 'form-control'}),
            'ordenTrabajo': forms.Select(attrs={'class': 'form-control'}),
            'estadoReparacion': forms.Select(attrs={'class': 'form-control'}),
            'estadoApro': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'descripActi': 'Descripción',
            'fecha':'',
            'horaIni':'',
            'jefe':'Jefe',
            'codequipo':'Código equipo',
            'empleado':'Empleado',
            'ordenTrabajo':'Orden de trabajo',
            'estadoReparacion': 'Estado de reparación',
            'estadoApro':'Estado de aprobación',
        
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }
        labels = {
            'username':'Usuario',
            'password':'Contraseña',
        }

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'codEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
            'departamento' : forms.Select(attrs={'class': 'form-control'}),
            'jefe': forms.Select(attrs={'class': 'form-control'}),
            'descPuesto': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'codEmpleado':'Código de Empleado',
            'nombres': 'Nombre',
            'apellidos': 'Apellido',
            'departamento': 'Departamento',
            'jefe': 'Coordinaror',
            'descPuesto': 'Puesto',
        }

class JefeForm(ModelForm):
    class Meta:
        model = Jefe
        fields = '__all__'
        widgets = {
            'codJefe':forms.TextInput(attrs={'class': 'form-control'}),
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'apellido':forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'codJefe':'Código Coordinador',
            'nombre':'Nombre',
            'apellido':'Apellido'
        }

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'codEquipo':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcionEqui':forms.TextInput(attrs={'class': 'form-control'}),
            'codFamilia':forms.Select(attrs={'class': 'form-control'}),
    }
    labels = {
        'codEquipo':'',
        'descripcionEqui':'',
        'codFamilia':'Código de Familia',
    }

class OrdenTrabajoForm(ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        widgets = {
            'codOrdenTrab': forms.TextInput(attrs={'class': 'form-control'}),
            'descOrden' : forms.TextInput(attrs={'class': 'form-control'}),
            'codEquipo':forms.Select(attrs={'class': 'form-control'}),
            'estado':forms.Select(attrs={'class': 'form-control'}),
        }
        label = {
            'codOrdenTrab':'',
            'descOrden':'',
            'codEquipo':'Código de equipo',
            'estado':'Estado',
        }

class FamiliaVehiculoForm(ModelForm):
    class Meta:
        model = FamiliaVehiculo
        fields = '__all__'
        widgets = {
            'descripcionFamilia': forms.TextInput(attrs={'class': 'form-control'}),
        }


