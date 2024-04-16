from django import forms
from django.core.exceptions import ValidationError
from .models import Habitacion, Categoria
from PIL import Image


def validate_square_image(image):
    img = Image.open(image)
    width, height = img.size
    if width != height:
        raise ValidationError('La imagen debe ser cuadrada.')
    
class NuevoHabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen',)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nombre de la habitación'}))
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'placeholder': 'Descripción de la habitación'}))
    precio = forms.FloatField(label='Precio', widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'step': '0.01'}))
    imagen = forms.ImageField(validators=[validate_square_image], label='Imagen')

class EliminarHabitacionForm(forms.Form):
    # categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoria')
    habitacion = forms.ModelChoiceField(queryset=Habitacion.objects.all(), label='Habitación')



