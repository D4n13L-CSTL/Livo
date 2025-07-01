from django.shortcuts import render
from .models import Club, AdministradorClub, ClubAtleta
from .serializer import ClubSerializer, AdministradorClubSerializer, RegistroClubSerializer, VerAtletasRegister
from rest_framework import viewsets, status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response





# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
class AdministradorClubViewSet(viewsets.ModelViewSet):
    queryset = AdministradorClub.objects.all()
    serializer_class = AdministradorClubSerializer


class RegistroClubView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        request=RegistroClubSerializer,
        responses={201: None}
    )
    
    def post(self, request):
        serializer = RegistroClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Club registrado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





class ClubQueryView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        serial = request.query_params.get('serial_club')
        if serial:
            try:
                club = Club.objects.get(serial_club=serial)
                serializer = ClubSerializer(club)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Club.DoesNotExist:
                return Response({'error': 'Club no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Parámetro serial_club requerido'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class Club_Atletas_register(APIView):
    def get(self,request):
        serial_club_cookie = request.COOKIES.get('serial_club')
        club_id = Club.objects.get(serial_club = serial_club_cookie)
        club_id_pritnt = club_id.id
        club = ClubAtleta.objects.filter(club = club_id_pritnt)
        serializer = VerAtletasRegister(club, many = True)
        return Response (serializer.data, status=status.HTTP_200_OK)