from django.db import models

# Create your models here.    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen=models.ImageField(upload_to="plan", null=True)

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.TextField()
    versionGratuita = models.BooleanField()


    def __str__(self):
        return self.nombre