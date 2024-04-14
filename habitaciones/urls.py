from django.urls import path
from . import views

app_name = 'habitacion'

urlpatterns = [
    path('nuevo/', views.nuevo_habitacion, name='nuevo'),
    path('eliminar/', views.eliminar_habitacion, name='eliminar_habitacion'),
    path('<str:nombre_categoria>/', views.categoria, name='categoria'),
]



