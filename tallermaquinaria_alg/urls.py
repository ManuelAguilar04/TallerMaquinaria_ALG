"""tallermaquinaria_alg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app_forms import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #Reparacion
    path('reparacion/',login_required(views.reparacion), name='reparacion'),
    path('reparacion/guardar/',views.guardar_reparacion, name='guardar_reparacion'),
    path('reparacion/<int:id>/editar/',views.editar_reparacion, name='editar_reparacion'),
    path('reparacion/<int:id>/eliminar/',views.eliminar_reparacion, name='eliminar_reparacion'),
    #Login y Logout
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_then_login,name='logout'),
    # Equipo
    path('equipo/', views.equipo, name='equipo'),
    path('equipo/<int:codEquipo>/editar/', views.equipo, name='editar_equipo'),
    path('equipo/<int:codEquipo>/eliminar/', views.eliminar_equipo, name='eliminar_equipo'),
    #Jefe
    path('jefe/', views.jefe, name='jefe'),
    path('jefe/<int:codJefe>/editar/', views.jefe, name='editar_jefe'),
    path('jefe/<int:codJefe>/eliminar/', views.eliminar_jefe, name='eliminar_jefe'),
    #Empleado
    path('empleado/', views.empleado, name='empleado'),
    path('empleado/<int:codEmpleado>/editar/', views.empleado, name='editar_empleado'),
    path('empleado/<int:codEmpleado>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    # Orden de trabajo
    path('orden-de-trabajo/', views.ordentrabajo, name='orden-de-trabajo'),
    path('orden-de-trabajo/<int:codOrdenTrab>/editar/', views.ordentrabajo, name='editar_orden'),
    path('orden-de-trabajo/<int:codOrdenTrab>/eliminar/', views.eliminar_orden, name='eliminar_orden'),
    #familia
    path('familia-vehiculo/', views.familiavehiculo, name='familia'),
    path('familia-vehiculo/<int:id>/editar/', views.familiavehiculo, name='editar_familia'),
    path('familia-vehiculo/<int:id>/eliminar/', views.eliminar_familia, name='eliminar_familia'),
    # import
    path('importar/', views.orden_vista_import , name='importar_orden_vista'),
    path('importar-orden/', views.importar , name='importar_orden'),
    path('equipo-view/', views.equipo_vista_import , name='importar_equipo_vista'),
    path('importar-equipo/', views.importar_equipo , name='importar_equipo'),
    path('empleado-view/', views.empleado_vista_import , name='importar_empleado_vista'),
    path('importar-empleado/', views.importar_empleado, name='importar_empleado'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

