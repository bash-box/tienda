from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto


# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda.html")

def buscar(request):
    if request.GET["producto"]:
        producto = request.GET.get("producto")

        articulos = Articulos.objects.filter(nombre__icontains=producto).values  # Articulos.objects.filter(nombre=producto).values()
        return render(request, "resultado.html", {"articulos":articulos, "query":producto})

    else:
        mensaje = "No has introducido nada en la busqueda"
    return HttpResponse(mensaje)

# Uso de formularios simple
"""def contacto(request):
    if request.method == "POST":
        asunto = request.POST["asunto"]
        email_from = settings.EMAIL_HOST_USER
        mensaje = request.POST["mensaje"] + " " + request.POST["email"]
        recipient_list = ["ajsboxcl2@gmail.com"]
        try:
            send_mail(asunto, mensaje, email_from, recipient_list)
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            # Puedes registrar el error o enviar un mensaje de error al usuario
            return HttpResponse('Error al enviar el correo.')
        return render(request, "gracias.html")
    return render(request, "contacto.html")"""

# Uso de Forms API
def contacto(request):
    miFormulario = FormularioContacto(request.POST)

    if miFormulario.is_valid():
        infForm = miFormulario.cleaned_data
        send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['info@sutraatechnosoft.net'],)

        return render(request, "gracias.html")
    else:
        miFormulario = FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})