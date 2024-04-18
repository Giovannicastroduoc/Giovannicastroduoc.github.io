from django.shortcuts import render
from rest_framework import generics
from habitaciones.models import Categoria, Habitacion
from .serializers import CategoriaSerializer, HabitacionSerializer

# Create your views here.
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class HabitacionList(generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
