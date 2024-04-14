from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Habitacion, Categoria
from .forms import NuevoHabitacionForm, EliminarHabitacionForm
from django.http import JsonResponse


def user_in_habitacion_permisos(user):
    if user.is_superuser:
        return True
    return user.groups.filter(name='permisos_habitaciones').exists()

# Create your views here.
def categoria(request, nombre_categoria):
    habitaciones = Habitacion.objects.all()
    categoria = Categoria.objects.get(nombre=nombre_categoria)

    return render(request, "habitaciones/categoria.html", {
        'categoria': categoria,
        'habitaciones': habitaciones,
    })




@login_required
@user_passes_test(user_in_habitacion_permisos, login_url='/')
def nuevo_habitacion(request):
    if request.method == 'POST':
        form = NuevoHabitacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Habitacion guardada exitosamente')
            return redirect('/habitaciones/nuevo')
        else:
            messages.error(request, 'No se pudo guardar la habitacion. Por favor, corrija los errores en el formulario.')
    else:
        form = NuevoHabitacionForm()

    return render(request, 'habitaciones/form.html', {
        'form': form,
        'title': 'Agregar Habitacion',
    })

@login_required
@user_passes_test(user_in_habitacion_permisos, login_url='/')
def eliminar_habitacion(request):
    if request.method == 'POST':
        form = EliminarHabitacionForm(request.POST)
        if form.is_valid():
            habitacion = form.cleaned_data['habitacion']
            habitacion.delete()
            messages.success(request, 'Habitacion eliminada exitosamente.')
            return redirect('games:eliminar_habitacion')
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


