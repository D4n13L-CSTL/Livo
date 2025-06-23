from django.shortcuts import render
from .serializer import DeporteSerializer
from .models import Deporte
from rest_framework import viewsets
# Create your views here.
#ESTA OPCION SERA PARA LOS ADMINISTRADORES DE LA PLATAFORMA 

class DeporteViewSet(viewsets.ModelViewSet):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer