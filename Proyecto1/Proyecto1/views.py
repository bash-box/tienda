from datetime import datetime, timezone
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

#hola  dsfdfdfdfdfdf


def saludo(request):
    return HttpResponse("Hola")

def bye(request):
    return HttpResponse("bye")

def producto(request):
    return HttpResponse("Producto Magy")

def suma(request, val1, val2):
    return HttpResponse(val1 + val2)

def get_alumno(request, id):
    if (id==1):
        return HttpResponse("El alumno es: Pepe")
    elif (id==2):
        return HttpResponse("El alumno es: Jose")


"""def mostrar(request):
    return render(request, "/home/x/Escritorio/Proyectos-Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")"""
def home(request):
    nombre = "pepe"
    lista = ["Uno", "Dos", "Tres"]
    return render(request, "home.html", {"nombre": nombre})

def quienes(request):
    nombre = "pepe"
    lista = ["Rojo","Verde","Amarillo"]
    return render(request, "quienes.html", {"nombre":nombre, "lista":lista})

def curso_c(request):
    fecha_actual = datetime.now().date()
    return render(request, "CursoC.html", {"dame_fecha":fecha_actual})

def curso_python(request):
    fecha_actual = datetime.now().date()
    return render(request, "curso-python.html", {"dame_fecha":fecha_actual})