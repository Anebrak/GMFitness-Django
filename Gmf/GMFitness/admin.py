from django.contrib import admin
from .models import *

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['nombre_usuario', 'numero_identidad', 'telefono', 'email', 'password']
    search_fields = ['nombre_usuario', 'numero_identidad', 'telefono', 'email']
    list_editable = ['telefono']


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['numero_identidad', 'peso', 'altura', 'edad', 'sexo', 'porcentajegraso']
    search_fields = ['numero_identidad__nombre_usuario', 'numero_identidad__numero_identidad']
    list_filter = ['sexo']
    list_editable = ['peso', 'porcentajegraso']


@admin.register(Nutrisionistas)
class NutricionistasAdmin(admin.ModelAdmin):
    list_display = ['numero_identidad', 'num_clientes']
    search_fields = ['numero_identidad__nombre_usuario', 'numero_identidad__numero_identidad']


@admin.register(Entrenadores)
class EntrenadoresAdmin(admin.ModelAdmin):
    list_display = ['numero_identidad', 'num_clientes']
    search_fields = ['numero_identidad__nombre_usuario', 'numero_identidad__numero_identidad']


@admin.register(Fisioterapeutas)
class FisioterapeutasAdmin(admin.ModelAdmin):
    list_display = ['numero_identidad', 'num_clientes']
    search_fields = ['numero_identidad__nombre_usuario', 'numero_identidad__numero_identidad']


# Tablas relacionales a Entrenador

@admin.register(Ejercicios)
class EjerciciosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_ejercicios', 'musculo', 'descripcion']
    search_fields = ['nombre_ejercicios', 'musculo']
    list_filter = ['musculo']


@admin.register(Rutinas)
class RutinasAdmin(admin.ModelAdmin):
    list_display = ['id', 'fechaInicio', 'fechaFin', 'ejercicio']
    search_fields = ['ejercicio__nombre_ejercicios']
    list_filter = ['fechaInicio', 'fechaFin']


@admin.register(AsignarRutinas)
class AsignarRutinasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'entrenador', 'rutina', 'semanas', 'dias', 'estado_rutina']
    search_fields = ['cliente__numero_identidad__nombre_usuario', 'entrenador__numero_identidad__nombre_usuario']
    list_filter = ['estado_rutina']
    list_editable = ['estado_rutina']


@admin.register(HistorialEjercicios)
class HistorialEjerciciosAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'rutina']
    search_fields = ['rutina__cliente__numero_identidad__nombre_usuario']
    list_filter = ['fecha']


# Tablas relacionales a Nutricionista

@admin.register(Alimentos)
class AlimentosAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigoBarras', 'proteina', 'grasas', 'kCal']
    search_fields = ['codigoBarras']


@admin.register(Dietas)
class DietasAdmin(admin.ModelAdmin):
    list_display = ['id', 'fechaInicio', 'fechaFin', 'alimento']
    search_fields = ['alimento__codigoBarras']
    list_filter = ['fechaInicio', 'fechaFin']


@admin.register(AsignarDietas)
class AsignarDietasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'nutrisionista', 'dieta', 'kCaloriasTotales', 'estado_dieta']
    search_fields = ['cliente__numero_identidad__nombre_usuario', 'nutrisionista__numero_identidad__nombre_usuario']
    list_filter = ['estado_dieta']


@admin.register(ProgresoClientes)
class ProgresoClientesAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha']
    search_fields = ['cliente__numero_identidad__nombre_usuario']
    list_filter = ['fecha']


# Fisioterapeuta

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fisioterapeuta', 'fechaInicio', 'fechaFin', 'estado']
    search_fields = ['cliente__numero_identidad__nombre_usuario', 'fisioterapeuta__numero_identidad__nombre_usuario']
    list_filter = ['estado', 'fechaInicio']
    list_editable = ['estado']


# Pagos y Membresías

@admin.register(Membresias)
class MembresiasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'tipos', 'precio', 'fecha_inicio', 'fecha_fin']
    search_fields = ['cliente__numero_identidad__nombre_usuario']
    list_filter = ['tipos', 'fecha_inicio']


@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = ['id', 'membresia', 'monto', 'echa', 'estado']
    search_fields = ['membresia__cliente__numero_identidad__nombre_usuario']
    list_filter = ['estado', 'echa']
    list_editable = ['estado']


@admin.register(Facturas)
class FacturasAdmin(admin.ModelAdmin):
    list_display = ['numFactura', 'fechaFactura', 'total', 'pagos', 'detalleFactura']
    search_fields = ['numFactura', 'detalleFactura']
    list_filter = ['fechaFactura']