from django.shortcuts import render
from django.http import HttpResponse
from .serializer import AtletaDeporteSerializer, AtletaSerializer
from .models import Atleta, AtletaDeporte
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
