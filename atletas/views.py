from django.shortcuts import render
from django.http import HttpResponse
from .serializer import AtletaDeporteSerializer, AtletaSerializer, RegistroAtletaSerializer
from .models import Atleta, AtletaDeporte
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


# Create your views here.
class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class AtletaDeporteViewSet(viewsets.ModelViewSet):
    queryset = AtletaDeporte.objects.all()
    serializer_class = AtletaDeporteSerializer



class RegistroAtletaView(APIView):
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