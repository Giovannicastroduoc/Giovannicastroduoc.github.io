from django.contrib import admin
from .models import Categoria, Habitacion
# Register your models here.

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","categoria"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria"]

admin.site.register(Categoria)
admin.site.register(Habitacion,HabitacionAdmin)
