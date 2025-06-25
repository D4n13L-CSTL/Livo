from django.shortcuts import render
from .models import Club, AdministradorClub
from .serializer import ClubSerializer, AdministradorClubSerializer, RegistroClubSerializer
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
    
