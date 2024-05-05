from django import forms
from django.core.exceptions import ValidationError
from .models import Habitacion, Categoria
from PIL import Image
from .models import Reserva

# Función de validación para asegurarse de que la imagen sea cuadrada
def validate_square_image(image):
    img = Image.open(image)
    width, height = img.size
    if width != height:
        raise ValidationError('La imagen debe ser cuadrada.')

# Formulario para crear una nueva habitación
class NuevoHabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen',)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre de la habitación'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'placeholder': 'Descripción de la habitación'}))
    precio = forms.FloatField(label='Precio', widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'step': '0.01'}))
    imagen = forms.ImageField(validators=[validate_square_image], label='Imagen')

# Formulario para eliminar una habitación
class EliminarHabitacionForm(forms.Form):
    habitacion = forms.ModelChoiceField(queryset=Habitacion.objects.all(), label='Habitación')

# Formulario para crear una reserva
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin']

    fecha_inicio = forms.DateField(label='Fecha de inicio', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(attrs={'type': 'date'}))


