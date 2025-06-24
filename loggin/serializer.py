# usuarios/serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Agregar datos extra al response
        data['tipo_usuario'] = self.user.tipo_usuario
        data['email'] = self.user.email
        data['username'] = self.user.username

        return data 
