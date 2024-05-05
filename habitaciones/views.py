from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Habitacion, Categoria, Reserva
from .forms import NuevoHabitacionForm, EliminarHabitacionForm, ReservaForm

# Función para verificar si el usuario tiene permisos de habitación
def user_in_habitacion_permisos(user):
    if user.is_superuser:
        return True
    return user.groups.filter(name='permisos_habitaciones').exists()


# Vista para mostrar las habitaciones de una categoría
def categoria(request, nombre_categoria):
    habitaciones = Habitacion.objects.filter(categoria__nombre=nombre_categoria)
    categoria = get_object_or_404(Categoria, nombre=nombre_categoria)
    return render(request, "habitaciones/categoria.html", {
        'categoria': categoria,
        'habitaciones': habitaciones,
    })


# Vista para agregar una nueva habitación
@login_required
@user_passes_test(user_in_habitacion_permisos, login_url='/')
def nuevo_habitacion(request):
    if request.method == 'POST':
        form = NuevoHabitacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitacion guardada exitosamente')
            return redirect('habitacion:nuevo')
        else:
            messages.error(request, 'No se pudo guardar la habitacion. Por favor, corrija los errores en el formulario.')
    else:
        form = NuevoHabitacionForm()

    return render(request, 'habitaciones/form.html', {
        'form': form,
        'title': 'Agregar Habitacion',
    })


# Vista para eliminar una habitación
@login_required
@user_passes_test(user_in_habitacion_permisos, login_url='/')
def eliminar_habitacion(request):
    if request.method == 'POST':
        form = EliminarHabitacionForm(request.POST)
        if form.is_valid():
            habitacion = form.cleaned_data['habitacion']
            habitacion.delete()
            messages.success(request, 'Habitacion eliminada exitosamente.')
            return redirect('habitacion:eliminar_habitacion')
        else:
            messages.error(request, 'Error, no se pudo eliminar el habitacion')
            categoria_id = request.POST.get("categoria")
            if categoria_id:
                form.fields['habitacion'].queryset = Habitacion.objects.filter(categoria_id=categoria_id)
    else:
        form = EliminarHabitacionForm()

    return render(request, 'habitaciones/form_eliminar.html', {
        'form': form,
        'title': 'Eliminar Habitacion',
    })


# Vista para buscar habitaciones
def buscar_habitaciones(request):
    query = request.GET.get('q')
    habitaciones = Habitacion.objects.filter(nombre__icontains=query)
    context = {
        'query': query,
        'habitaciones': habitaciones
    }
    return render(request, 'habitaciones/busqueda.html', context)


# Vista para reservar una habitación
@login_required
def reservar_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.habitacion = habitacion
            reserva.usuario = request.user
            reserva.save()

            return redirect('habitacion:pagina_confirmacion', reserva_id=reserva.id)
    else:
        form = ReservaForm()
    return render(request, 'habitaciones/reservar_habitacion.html', {'form': form, 'habitacion_id': habitacion_id})


# Vista para mostrar la página de confirmación de reserva
def pagina_confirmacion(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'habitaciones/pagina_confirmacion.html', {'reserva': reserva})


# Vista para mostrar las reservas de un usuario
@login_required
def vista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'habitaciones/reservas.html', {'reservas': reservas})


# Vista para cancelar una reserva
@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.user == reserva.usuario or request.user.is_superuser:
        reserva.delete()
        messages.success(request, 'Reserva cancelada exitosamente.')
    else:
        messages.error(request, 'No tienes permiso para cancelar esta reserva.')

    if request.user.is_superuser:
        return redirect('habitacion:reservas_todas')
    else:
        return redirect('habitacion:vista_reservas')


# Vista para mostrar todas las reservas (solo para superusuarios)
@login_required
def reservas_todas(request):
    if not request.user.is_superuser:
        return redirect('habitacion:vista_reservas')  # Redirigir a la vista de reservas del usuario si no es un superusuario
    reservas = Reserva.objects.all()
    return render(request, 'habitaciones/reservas_todas.html', {'reservas': reservas})
