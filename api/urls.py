from django.urls import path
from .import views

urlpatterns = [
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('habitaciones/', views.HabitacionList.as_view(), name='habitacion-list'),
]
