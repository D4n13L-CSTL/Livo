from django.shortcuts import render
from .models import Club, AdministradorClub
from .serializer import ClubSerializer, AdministradorClubSerializer
from rest_framework import viewsets
# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
class AdministradorClubViewSet(viewsets.ModelViewSet):
    queryset = AdministradorClub.objects.all()
    serializer_class = AdministradorClubSerializer
