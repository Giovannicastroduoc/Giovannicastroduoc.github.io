from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete

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
        return [{"id": room.id, "nombre": room.nombre} for room in self.habitaciones.all()]

class Habitacion(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='habitaciones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='habitacion_imagenes', blank=True, null=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Reserva de {self.habitacion} para {self.usuario}"

@receiver(post_delete, sender=Habitacion)
def delete_habitacion_image(sender, instance, **kwargs):
    instance.imagen.delete(save=False)
