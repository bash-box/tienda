from django.urls import path
from ProyectoWebApp import views

app_name="carro"

urlpatterns = [
    path('agregar/<int:producto_id/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id/', views.restar_producto, name="restar"),
    path('restar/', views.limpiar_carro, name="limpíar"),
]
