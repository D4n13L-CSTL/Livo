from django.shortcuts import render
from .serializer import EventoCalendarioSerializer
from rest_framework import viewsets
from .models import EventoCalendario
# Create your views here.


class EventoCalendarioViewSet(viewsets.ModelViewSet):
    queryset = EventoCalendario.objects.all()
    serializer_class = EventoCalendarioSerializer