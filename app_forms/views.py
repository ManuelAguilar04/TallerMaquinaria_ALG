import io
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import  Equipo, Jefe, Empleado, Reparacion, OrdenTrabajo, FamiliaVehiculo
from .forms import ReparacionForm, LoginForm, EquipoForm, JefeForm, EmpleadoForm, OrdenTrabajoForm, FamiliaVehiculoForm
from django.views.generic import View
from django.conf import settings
from django.views.generic.base import TemplateView
from django.urls import NoReverseMatch, reverse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from tablib import Dataset 
from .resource import OrdenTrabajoResource, EquipoResource, EmpleadoResource

@login_required
def index(request):
    reparaciones = Reparacion.objects.all()
    ctx = {
        'reparaciones':reparaciones
    }
    return render(request, 'index.html', ctx)

@login_required
def reparacion(request):
    form = ReparacionForm()
    return render(request, 'reparacion.html', {'form': form})

def guardar_reparacion(request):
    if request.method == 'POST':
        form = ReparacionForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Se ha registrado la reparación con éxito')

            return redirect('reparacion')
        else:
            return render(request, 'reparacion.html', {'form': form})

def editar_reparacion(request, id=None): 
        reparacion = Reparacion.objects.all()

        if request.method == 'GET':
            reparacion = get_object_or_404(Reparacion, pk=id)if id else None

            form = ReparacionForm(instance=reparacion)
            ctx = {
                'form':form,
                'reparacion':reparacion,
                'id':id
            }
            return render(request, 'reparacion.html',ctx)
        else:
            reparacion = reparacion = get_object_or_404(Reparacion, pk=id)if id else None
            form = ReparacionForm(request.POST or None, instance=reparacion)

            if form.is_valid():
                form.save()
                if id:
                    messages.add_message(request, messages.SUCCESS,'Se ha actualizado la reparación')
                else:
                    messages.add_message(request, messages.SUCCESS,'Se ha registrado la reparación')

                return redirect('/')
            else:
                return render(request, 'reparacion.html', {'form': form, 'reparacion': reparacion})

def eliminar_reparacion(request, id):
    reparacion = Reparacion.objects.get(pk=id) 
    acti = reparacion.descripActi

    reparacion.delete()
    messages.add_message(request, messages.ERROR, f'La reparación {acti} ha sido eliminado con éxito')
    return redirect('/')

def login(request):
        if request.method=='POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get("username")
                password=form.cleaned_data.get(password)
                username = authenticate(username=username, password=password)
                if username is not None:
                    login(request,username)
                    messages.success(request, F"Bienvenido {username}")
                    return redirect("index")
                form = AuthenticationForm()
                return render(request, "login.html",{"form":form})
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

@permission_required('app_forms.is_coordinador')
def equipo(request, codEquipo=None):
    equipos = Equipo.objects.all().order_by('codEquipo')

    if request.method == 'GET':
        equipo = get_object_or_404(Equipo, pk=codEquipo) if codEquipo else None

        form = EquipoForm(instance=equipo)

        ctx = {
            'form':form,
            'equipos':equipos,
            'codEquipo': codEquipo
        }

        return render(request, 'equipo.html', ctx)

    else:
            equipo = get_object_or_404(Equipo, pk=codEquipo) if codEquipo else None
            form = EquipoForm(request.POST or None, instance=equipo)

            if form.is_valid():
                form.save()

                if codEquipo :
                    messages.add_message(request, messages.SUCCESS, 'Se ha actualizado el equipo con éxito')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Se ha registrado el equipo con éxito')

                return redirect('equipo')
            else:
                return render(request, 'equipo.html', {'form':form, 'equipos':equipos})


def eliminar_equipo(request, codEquipo):
    equip = Equipo.objects.get(pk=codEquipo) 
    codigo = equip.codEquipo

    equip.delete()
    messages.add_message(request, messages.ERROR, f'El equipo {codigo} se a eliminado con éxito')
    return render(request, 'equipo.html')

@permission_required('app_forms.is_jefe')
def jefe(request, codJefe=None):
    jefes = Jefe.objects.all().order_by('codJefe')

    if request.method == 'GET':
        jefe = get_object_or_404(Jefe, pk=codJefe) if codJefe else None

        form = JefeForm(instance=jefe)

        ctx = {
            'form':form,
            'jefes':jefes,
            'codJefe': codJefe
        }

        return render(request, 'jefe.html', ctx)

    else:
            jefe = get_object_or_404(Jefe, pk=codJefe) if codJefe else None
            form = JefeForm(request.POST or None, instance=jefe)

            if form.is_valid():
                form.save()

                if codJefe :
                    messages.add_message(request, messages.SUCCESS, 'Se ha actualizado el coordinador con éxito')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Se ha registrado el coordinador con éxito')

                return redirect('jefe')
            else:
                return render(request, 'jefe.html', {'form':form, 'jefes':jefes})

def eliminar_jefe(request, codJefe):
    jef = Jefe.objects.get(pk=codJefe) 
    codigo = jef.codJefe

    jef.delete()
    messages.add_message(request, messages.ERROR, f'El jefe {codigo} se a eliminado con éxito')
    return render(request, 'jefe.html')

@permission_required('app_forms.is_coordinador')
def empleado(request, codEmpleado=None):
    empleados = Empleado.objects.all().order_by('codEmpleado')

    if request.method == 'GET':
        empleado = get_object_or_404(Empleado, pk=codEmpleado) if codEmpleado else None

        form = EmpleadoForm(instance=empleado)

        ctx = {
            'form':form,
            'empleados':empleados,
            'codEmpleado': codEmpleado
        }

        return render(request, 'empleado.html', ctx)

    else:
            empleado = get_object_or_404(Empleado, pk=codEmpleado) if codEmpleado else None
            form =EmpleadoForm(request.POST or None, instance=empleado)

            if form.is_valid():
                form.save()

                if codEmpleado :
                    messages.add_message(request, messages.SUCCESS, 'Se ha actualizado el empleado con éxito')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Se ha registrado el empleado con éxito')

                return render('empleado')
            else:
                return render(request, 'empleado.html', {'form':form, 'empleados':empleados})

def eliminar_empleado(request, codEmpleado):
    emp = Empleado.objects.get(pk=codEmpleado) 
    codigo = emp.codEmpleado

    emp.delete()
    messages.add_message(request, messages.ERROR, f'El empleado {codigo} se a eliminado con éxito')
    return render(request, 'empleado.html')

@permission_required('app_forms.is_coordinador')
def ordentrabajo(request, codOrdenTrab=None):
    ordenes = OrdenTrabajo.objects.all().order_by('codOrdenTrab')

    if request.method == 'GET':
        orden = get_object_or_404(OrdenTrabajo, pk=codOrdenTrab) if codOrdenTrab else None

        form = OrdenTrabajoForm(instance=orden)

        ctx = {
            'form':form,
            'ordenes':ordenes,
            'codOrdenTrab': codOrdenTrab
        }

        return render(request, 'ordentrabajo.html', ctx)

    else:
            orden = get_object_or_404(OrdenTrabajo, pk=codOrdenTrab) if codOrdenTrab else None
            form = OrdenTrabajoForm(request.POST or None, instance=orden)

            if form.is_valid():
                form.save()

                if codOrdenTrab :
                    messages.add_message(request, messages.SUCCESS, 'Se ha actualizado la orden de trabajo con éxito')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Se ha registrado la orden de trabajo con éxito')

                return redirect('orden-de-trabajo')
            else:
                return render(request, 'ordentrabajo.html', {'form':form, 'ordenes':ordenes})

def eliminar_orden(request, codJefe):
    ordn = OrdenTrabajo.objects.get(pk=codOrdenTrab) 
    codigo = ordn.descOrden

    ordn.delete()
    messages.add_message(request, messages.ERROR, f'La orden de {codigo} se a eliminado con éxito')
    return render(request, 'ordentrabajo.html')

@permission_required('app_forms.is_coordinador')
def familiavehiculo(request, id=None):
    familias = FamiliaVehiculo.objects.all().order_by('id')

    if request.method == 'GET':
        familia = get_object_or_404(FamiliaVehiculo, pk=id) if id else None

        form = FamiliaVehiculoForm(instance=familia)

        ctx = {
            'form':form,
            'familias':familias,
            'id': id
        }

        return render(request, 'familiavehiculos.html', ctx)

    else:
            familia = get_object_or_404(FamiliaVehiculo, pk=id) if id else None
            form = FamiliaVehiculoForm(request.POST or None, instance=familia)

            if form.is_valid():
                form.save()

                if id :
                    messages.add_message(request, messages.SUCCESS, 'Se ha actualizado la familia vehiculo con éxito')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Se ha registrado la familia vehiculo con éxito')

                return redirect('familia')
            else:
                return render(request, 'familiavehiculos.html', {'form':form, 'familias':familias})

def eliminar_familia(request, id):
    fam = FamiliaVehiculo.objects.get(pk=id) 
    codigo = fam.descripcionFamilia

    fam.delete()
    messages.add_message(request, messages.ERROR, f'La familia {codigo} se a eliminado con éxito')
    return render(request, 'familiavehiculos.html')

@permission_required('app_forms.is_coordinador')
def orden_vista_import(request):
    trabajos = OrdenTrabajo.objects.all().order_by('codOrdenTrab')
    ctx = {
        'trabajos': trabajos
    }
    return render(request, 'importarOT.html', ctx)

@permission_required('app_forms.is_coordinador')
def importar(request):
    if request.method == 'POST':
        ordentrabajo_resource = OrdenTrabajoResource()  
        dataset = Dataset()  
        nuevas_orden = request.FILES['xlsfile']   

        if not nuevas_orden.name.endswith('xlsx'):
            messages.info(request, 'wrong format')  
            return render(request, 'importarOT.html')  

        imported_data = dataset.load(nuevas_orden.read(), format='xlsx')
        for data in imported_data:
            value = OrdenTrabajo(
                data[0],
                data[1],
                data[2],
                )
            value.save()
    return render(request,'importarOT.html')

@permission_required('app_forms.is_coordinador')
def equipo_vista_import(request):
    equipos = Equipo.objects.all().order_by('codEquipo')
    ctx = {
        'equipos': equipos
    }
    return render(request, 'importarequipo.html', ctx)

@permission_required('app_forms.is_coordinador')
def importar_equipo(request):
    if request.method == 'POST':
        equipo_resource = EquipoResource()  
        dataset = Dataset()  
        nuevos_equipos = request.FILES['xlsfile']   

        if not nuevos_equipos.name.endswith('xlsx'):
            messages.info(request, 'wrong format')  
            return render(request, 'importarequipo.html')  

        imported_data = dataset.load(nuevos_equipos.read(), format='xlsx')
        for data in imported_data:
            value = Equipo(
                data[0],
                data[1],
                data[2],
                )
            value.save()
    return render(request,'importarequipo.html')

@permission_required('app_forms.is_coordinador')
def empleado_vista_import(request):
    empleados = Empleado.objects.all().order_by('codEmpleado')
    ctx = {
        'empleados': empleados
    }
    return render(request, 'importarempleado.html', ctx)


def importar_empleado(request):
    if request.method == 'POST':
        empleado_resource = EmpleadoResource()  
        dataset = Dataset()  
        nuevos_empleados = request.FILES['xlsfile']   

        if not nuevos_empleados.name.endswith('xlsx'):
            messages.info(request, 'wrong format')  
            return render(request, 'importarempleado.html')  

        imported_data = dataset.load(nuevos_empleados.read(), format='xlsx')
        for data in imported_data:
            value = Empleado(
                data[0],
                data[1],
                data[2],
                data[3],
                )
            value.save()
    return render(request,'importarempleado.html')