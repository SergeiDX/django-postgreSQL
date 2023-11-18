from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100, null=False, verbose_name="Empresa")
    fundacion  = models.DateField(null=False, verbose_name="Fundacion")
    sitio_web = models.CharField(max_length=100,null=False,verbose_name="Sitio Web")
    pais_origen = models.CharField(max_length=100,null=False,verbose_name="Pais Origen")
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fehca_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.nombre_empresa
    
    class Meta:
        db_table = "empresa"
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ["id"]
        
class Desarrollador(models.Model):
    nombre_desarrollador = models.CharField(max_length=100, null=False, verbose_name="Desarrollador")
    fundacion = models.DateField(null=False, verbose_name="Fundacion")
    pais_origen = models.CharField(max_length=100, null=False, verbose_name="Pais Origen")
    sitio_web = models.CharField(max_length=100, null=False, verbose_name="Sitio Web")
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.nombre_desarrollador
    
    class Meta:
        db_table = "desarrollador"
        verbose_name = "desarrollador"
        verbose_name_plural = "desarrolladores"
        ordering = ["id"]
     
class contrato(models.Model):
    descripcion_contrato = models.CharField(max_length=100, null=False, verbose_name="Descripcion del contrato")
    fecha_inicio = models.DateField(null=False, verbose_name="Fecha inicio de contrato")
    fecha_limite = models.DateField(null=False, verbose_name="Fecha limite de contrato")
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.descripcion_contrato
    
    class Meta:
        db_table = "contrato"
        verbose_name = "contrato"
        verbose_name_plural = "contratos"
        ordering = ["id"]
        
class Videojuegos(models.Model):
    titulo_videojuego = models.CharField(max_length=100, null=False, verbose_name="Titulo videojuego")
    lanzamiento = models.DateField(null=False, verbose_name="Lanzamiento")
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.titulo_videojuego
    
    class Meta:
        db_table = "videojuegos"
        verbose_name = "videojuego"
        verbose_name_plural = "videojuegos"
        ordering = ["id"]
        
class Usuarios(models.Model):
    username = models.CharField(max_length=100, null=False, verbose_name="Nombre de usuario")
    correo = models.CharField(max_length=100, null=False, verbose_name="Correo")
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "usuarios"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["id"]
    
class Plataformas(models.Model):
    nombre_plataforma = models.CharField(max_length=100, null=False, verbose_name="Plataforma")
    fabricante = models.CharField(max_length=100, null=False, verbose_name="Fabricante")
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE, null=True, blank=True)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.nombre_plataforma
    
    class Meta:
        db_table = "plataformas"
        verbose_name = "plataforma"
        verbose_name_plural = "plataformas"
        ordering = ["id"]
        
class Clasificacion(models.Model):
    clasificacion = models.CharField(max_length=100, null=False, verbose_name="Clasificacion")
    tipo_clasificacion = models.CharField(max_length=100, null=False, verbose_name="Tipo de Clasificacion")
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.clasificacion
    
    class Meta:
        db_table = "clasificacion"
        verbose_name = "clasificacion"
        verbose_name_plural = "clasificacion"
        ordering = ["id"]
        
class Genero(models.Model):
    nombre_genero = models.CharField(max_length=100, null=False, verbose_name="Nombre del genero")
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE, null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.nombre_genero
    
    class Meta:
        db_table = "genero"
        verbose_name = "genero"
        verbose_name_plural = "generos"
        ordering = ["id"]
    
    
class Ventas(models.Model):
    precio = models.DecimalField(max_digits=10,decimal_places=2,null=False,verbose_name="Precio")
    fecha_venta = models.DateField(null=False, verbose_name="Fecha de venta")
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    class Meta:
        db_table = "ventas"
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        ordering = ["id"]

class Tiendas(models.Model):
    nombre_tienda = models.CharField(max_length=100, null=False, verbose_name="Nombre de la tienda")
    videojuego = models.ForeignKey(Videojuegos, on_delete=models.CASCADE, null=True, blank=True)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Alta")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    
    def __str__(self):
        return self.nombre_tienda
    
    class Meta:
        db_table = "tiendas"
        verbose_name = "tienda"
        verbose_name_plural = "tiendas"
        ordering = ["id"]