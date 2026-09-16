from django.db import models

class Usuarios(models.Model):
    numero_identidad = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre_usuario} ({self.numero_identidad})"

# Tipos de Usuarios 
class Nutrisionistas(models.Model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Entrenadores(models.Model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Fisioterapeutas(models.Model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Clientes(models.Model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    edad = models.IntegerField()
    
    SEXO = (
        ("0", "Hombre"),
        ("1", "Mujer"),
        ("2", "Otro"),
    )
    sexo = models.CharField(max_length=1, choices=SEXO)
    porcentajegraso = models.DecimalField(max_digits=5, decimal_places=2)

# Tablas relacionales a entrenador

class Ejercicios(models.Model): 
    nombre_ejercicios = models.CharField(max_length=225)
    musculo = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=500)

class Rutinas(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    ejercicio = models.ForeignKey(Ejercicios, on_delete=models.DO_NOTHING)

class AsignarRutinas(models.Model):
    semanas = models.IntegerField()
    dias = models.IntegerField()
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    intensidad = models.CharField(max_length=50)
    
    ESTADO = (
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    )
    estado_rutina = models.CharField(max_length=20, choices=ESTADO)
    entrenador = models.ForeignKey(Entrenadores, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    rutina = models.ForeignKey(Rutinas, on_delete=models.DO_NOTHING)

class HistorialEjercicios(models.Model):
    fecha = models.DateField()
    rutina = models.ForeignKey(AsignarRutinas, on_delete=models.DO_NOTHING)

# Tablas relacionales a nutricionista

class Alimentos(models.Model):
    codigoBarras = models.CharField(max_length=100)
    proteina = models.DecimalField(max_digits=6, decimal_places=2)
    grasas = models.DecimalField(max_digits=6, decimal_places=2)
    kCal = models.DecimalField(max_digits=6, decimal_places=2)

class Dietas(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    alimento = models.ForeignKey(Alimentos, on_delete=models.DO_NOTHING)
    
class AsignarDietas(models.Model):
    carbosTotales = models.DecimalField(max_digits=6, decimal_places=2)
    kCaloriasTotales = models.DecimalField(max_digits=6, decimal_places=2)
    proteinasTotales = models.DecimalField(max_digits=6, decimal_places=2)
    grasasTotales = models.DecimalField(max_digits=6, decimal_places=2)    
    
    estados_dieta = (
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    )
    estado_dieta = models.CharField(max_length=20, choices=estados_dieta)
    nutrisionista = models.ForeignKey(Nutrisionistas, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    dieta = models.ForeignKey(Dietas, on_delete=models.DO_NOTHING)

class ProgresoClientes(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    
# Fisioterapeuta    

class Citas(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()   
    
    ESTADO = (
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    )
    estado = models.CharField(max_length=20, choices=ESTADO)
    fisioterapeuta = models.ForeignKey(Fisioterapeutas, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)    

# Sección del apartado de pagos

class Membresias(models.Model):
    precio = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateField()
    
    TIPOS = (
        ("premium", "PREMIUM"),
        ("gratuita", "GRATUITA"),
    )
    tipos = models.CharField(max_length=20, choices=TIPOS, default="gratuita")
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)

class Pagos(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField()
    
    ESTADO = (
        ("pendiente", "PENDIENTE"),
        ("rechazado", "RECHAZADO"),
        ("confirmado", "CONFIRMADO"),
    )
    estado = models.CharField(max_length=20, choices=ESTADO, default="pendiente")
    membresia = models.ForeignKey(Membresias, on_delete=models.DO_NOTHING)

class Facturas(models.Model):
    numFactura = models.IntegerField(primary_key=True)
    detalleFactura = models.CharField(max_length=300)
    fechaFactura = models.DateField()
    total = models.IntegerField()
    pagos = models.ForeignKey(Pagos, on_delete=models.DO_NOTHING)