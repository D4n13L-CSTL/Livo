
# usuarios/serializers.p
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from atletas.models import AtletaDeporte
from clubes.models import Club  # Asegúrate de importar el modelo Club si es necesario  
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    tipo_usuario = serializers.CharField(write_only=True)
    def validate(self, attrs):
        print("Attrs recibidos:", attrs)
        tipo_usuario_enviado = attrs.pop('tipo_usuario', None)
        print("Tipo usuario enviado:", tipo_usuario_enviado)

        
        if 'username' in attrs and attrs['username']:
            attrs['username'] = attrs['username'].upper()
        data = super().validate(attrs)  # Validación username y password
        
        user = self.user
        
        if tipo_usuario_enviado.upper() != user.tipo_usuario:
            raise serializers.ValidationError("Tipo de usuario no coincide.")
        
        data['tipo_usuario'] = user.tipo_usuario
        data['email'] = user.email
        data['username'] = user.username
        
        if user.tipo_usuario == 'ATLETA':
            atleta = user.atleta.first()
            if atleta:
                deporte_rel = AtletaDeporte.objects.filter(atleta=atleta).first()
                if deporte_rel:
                    data['deporte'] = deporte_rel.deporte.nombre
                    data['nivel_habilidad'] = deporte_rel.nivel_habilidad
                    data['deporte_id'] = deporte_rel.deporte.id
                    data['id'] = atleta.id
                else:
                    data['deporte'] = None
                    data['nivel_habilidad'] = None
            else:
                data['deporte'] = None
                data['nivel_habilidad'] = None

        elif user.tipo_usuario == 'CLUB':
            admin_club = user.club.first()
            if admin_club:
                club = admin_club.club
                data['deporte'] = club.deporte.nombre
                data['deporte_id'] = club.deporte.id
                data['serial_club'] = club.serial_club
            else:
                data['deporte'] = None
                data['deporte_id'] = None

        return data