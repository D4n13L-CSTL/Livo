from rest_framework import serializers
from .models import EventoCalendario

class EventoCalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCalendario
        fields = '__all__'
        
