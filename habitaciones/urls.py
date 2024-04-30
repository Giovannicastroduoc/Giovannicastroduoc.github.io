from django.urls import path
from . import views

app_name = 'habitacion'

urlpatterns = [
    path('nuevo/', views.nuevo_habitacion, name='nuevo'),
    path('eliminar/', views.eliminar_habitacion, name='eliminar_habitacion'),
    path('<str:nombre_categoria>/', views.categoria, name='categoria'),
    path('busqueda/', views.buscar_habitaciones, name='buscar_habitaciones'),  # Cambiando la URL a 'busqueda/'
    path('reservar/<int:habitacion_id>/', views.reservar_habitacion, name='reservar_habitacion'),
    path('confirmacion/<int:reserva_id>/', views.pagina_confirmacion, name='pagina_confirmacion'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('habitaciones/vista_reservas/', views.vista_reservas, name='vista_reservas'),
]