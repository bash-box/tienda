from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

def home(request):
    return render(request, "home.html")





