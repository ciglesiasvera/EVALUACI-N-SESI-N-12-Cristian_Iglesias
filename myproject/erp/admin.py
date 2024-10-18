from django.contrib import admin
from .models import Producto, Fabrica

@admin.register(Fabrica)
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')
    list_filter = ('pais',) 

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'costo', 'fecha_vencimiento', 'fabrica')
    search_fields = ('nombre', 'fabrica__nombre')
    list_filter = ('nombre', 'fabrica')