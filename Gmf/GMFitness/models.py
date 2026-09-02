from django.db import models

# Create your models here.
class Usuarios(models.model):
    numero_identidad = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    telefono = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)

    def __str__self(self):
        return f"""Nombre: {self.nombre} 
        Email: {self.email}
        Numero identidad: {self.numeroIdentidad}
        """

# Tipos de Usuarios 
class Nutrisionistas(models.model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Entrenadores(models.model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Fisioterapeutas(models.model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    num_clientes = models.IntegerField()

class Clientes(models.model):
    numero_identidad = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    peso = models.DecimalField()
    altura = models.DecimalField()
    edad = models.IntegerField(max_length=100)
    #  Lista de Generos
    SEXO = (("0", "Hombre")
            ("1", "Mujer"),
            ("2", "Otro"))
    sexo = models.CharField(choices=SEXO)
    porcentajegraso = models.DecimalField()

# Tablas relacionales a entrenador

class Ejercicios(models.model): 
    nombre_ejercicios = models.CharField(max_length=225)
    musculo = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=500)

class Rutinas(models.model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    ejercicio = models.ForeignKey(Ejercicios, on_delete=models.DO_NOTHING)


class AsignarRutinas(models.model):
    semanas = models.IntegerField()
    dias = models.IntegerField()
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    intensidad = models.CharField()
    #Lista de las rutinas
    ESTADO=(("Activo"), ("ACTIVO"),
                 ("Inactivo"), ("INACTIVO"))
    estado_rutina = models.CharField(choices=ESTADO)
    entrenador = models.ForeignKey(Entrenadores, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    rutina = models.ForeignKey(Rutinas, on_delete=models.DO_NOTHING)

    

class HistorialEjercicios(models.model):
    fecha = models.DateField()
    #Agregar herecia de AsignarRutinas
    rutina = models.ForeignKey(AsignarRutinas, on_delete=models.DO_NOTHING)


# Tablas relacionales a nutrisionista


class Alimentos(models.model):
    codigoBarras = models.CharField()
    proteina = models.DecimalField()
    grasas = models.DecimalField()
    kCal = models.DecimalField()

class Dietas(models.model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    alimento = models.ForeignKey(Alimentos, on_delete=models.DO_NOTHING)
    
class AsignarDietas(models.model):
    carbosTotales = models.DecimalField()
    kCaloriasTotales = models.DecimalField()
    proteinasTotales = models.DecimalField()
    grasasTotales = models.DecimalField()    
    estado_dieta = models.CharField()
    #Lista de las dietas
    estados_dieta=(("Activo"), ("ACTIVO"),
                 ("Inactivo"), ("INACTIVO"))
    nutrisionista = models.ForeignKey(Nutrisionistas, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    dieta = models.ForeignKey(Dietas, on_delete=models.DO_NOTHING)

class ProgresoClientes(models.model):
    fecha = models.DateField()
    #Agregar herencias del campo cliente
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    
#Fisioterapeuta    

class Citas(models.model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()   
    #Lista de las estados
    ESTADO=(("Activo"), ("ACTIVO"),
                 ("Inactivo"), ("INACTIVO"))
    estado = models.CharField(choices=ESTADO)
    fisioterapeuta = models.ForeignKey(Fisioterapeutas, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)    



# Sección del apartado de pagos
class Membresias(models.model):
    precio = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateField()
    TIPOS = (("premiun", "PREMIUN"),
             ("gratuita"), ("GRATUITA"))
    tipos = models.CharField(choices=TIPOS, default="gratuita")
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)

class Pagos(models.model):
    monto = models.IntegerField()
    echa = models.DateField()
    ESTADO =(
            ("pendiente", "PENDIENTE")
            ("rechazado", "RECHAZADO")
            ("comfirmado", "COMFIRMADO")
                )
    estado = models.CharField(choices=ESTADO , default="pendiente")
    membresia = models.ForeignKey(Membresias, on_delete=models.DO_NOTHING)

class Facturas(models.model):
    numFactura = models.IntegerField(primary_key=True)
    detalleFactura = models.CharField(max_length=300)
    fechaFactura = models.DateField()
    total = models.IntegerField()
    pagos = models.ForeignKey(Pagos, on_delete=models.DO_NOTHING)
    
    
    







