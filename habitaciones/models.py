from django.db import models
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='categoria_imagenes', blank=True, null=True)
    background = models.ImageField(upload_to='categoria_imagenes', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre
    def get_rooms_serialized(self):
        return [{"id": room.id, "nombre": room.nombre} for room in self.juegos.all()]

class Habitacion(models.Model):
    categoria = models.ForeignKey(Categoria, related_name = 'categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='habitacion_imagenes', blank=True, null=True)

    class Meta:
        ordering=('nombre', )

    def __str__(self):
        return self.nombre

    
def delete_habitacion_image(sender, instance, **kwargs):
    instance.imagen.delete(save=False)

post_delete.connect(delete_habitacion_image, sender=Habitacion)