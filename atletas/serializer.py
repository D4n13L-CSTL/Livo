from rest_framework import serializers
from .models import Atleta, AtletaDeporte

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'
        
class AtletaDeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtletaDeporte
        fields = '__all__'
    
 