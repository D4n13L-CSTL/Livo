from django.shortcuts import render
from django.http import HttpResponse
from .serializer import AtletaDeporteSerializer, AtletaSerializer, RegistroAtletaSerializer, ClubSerializer,ClubAtletaSerializer, InscripcionesSerializer
from .models import Atleta, AtletaDeporte
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from clubes.models import Club, ClubAtleta



# Create your views here.
class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class AtletaDeporteViewSet(viewsets.ModelViewSet):
    queryset = AtletaDeporte.objects.all()
    serializer_class = AtletaDeporteSerializer


class RegistroAtletaView(APIView): #VIEW DE REGISTRAR ATLETA
    permission_classes = [AllowAny]
    @extend_schema(
        request=RegistroAtletaSerializer,
        responses={201: None}
    )
    
    def post(self, request):
        serializer = RegistroAtletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Atleta registrado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    





class AtletaxDeporte(APIView):

    @extend_schema(
            responses={201: None}
        )
    def get(self, request):
        deporte_cookie = request.COOKIES.get('deporte')
        id_deporte = request.COOKIES.get('id_deporte', None)
        print(f"Deporte desde la cookie: {id_deporte}")

        if not id_deporte:
            return Response({"detail": "No se encontró el id_deporte en la cookie."}, status=status.HTTP_400_BAD_REQUEST)

        clubes = Club.objects.filter(deporte_id=id_deporte)
        serializer = ClubSerializer(clubes, many=True)  # Necesitas definir un serializer si quieres retornar datos serializados

        return Response(serializer.data, status=status.HTTP_200_OK)
    






class PerfilAtletaView(APIView):
    @extend_schema(
        responses={200: AtletaSerializer}
    )
    def get(self, request):
        try:
            id_de_atleta = request.COOKIES.get('id_atleta', None)
            atleta = Atleta.objects.get(id=id_de_atleta)
            serializer = AtletaSerializer(atleta)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Atleta.DoesNotExist:
            return Response({"detail": "Atleta no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        
        

class RegisterClubView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        responses={201: None}
    )
    def post(self, request):
        serializer = ClubAtletaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Atleta Inscrito Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class VerificarInscripcionView(APIView):
    @extend_schema(
        responses={200: InscripcionesSerializer}
    )
    def get(self, request):
        atleta_id = request.COOKIES.get('id_atleta', None)
        if not atleta_id:
            return Response({"detail": "No se encontró el id del atleta en la cookie."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            inscripcion = ClubAtleta.objects.get(atleta_id=atleta_id, activo=True)
            serializer = InscripcionesSerializer(inscripcion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ClubAtleta.DoesNotExist:
            return Response({"detail": "El atleta no está inscrito en ningún club."}, status=status.HTTP_40_NOT_FOUND)