from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clientes
from gestionPedidos.models import Pedidos
from gestionPedidos.models import Articulos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "telefono")
    search_fields=("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",)

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos)
admin.site.register(Articulos, ArticulosAdmin)

