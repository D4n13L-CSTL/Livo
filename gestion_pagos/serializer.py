from rest_framework import serializers
from clubes.models import ClubAtleta


class ReportarPagoSerializer(serializers.Serializer):
    
    
    atleta = ''