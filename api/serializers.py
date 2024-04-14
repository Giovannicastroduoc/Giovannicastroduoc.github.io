from rest_framework import serializers
from habitaciones.models import Categoria, Habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    categoria = HabitacionSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'imagen', 'background', 'descripcion', 'categoria')
