# usuarios/serializers.p
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from atletas.models import AtletaDeporte
from clubes.models import Club  # Asegúrate de importar el modelo Club si es necesario  
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Agregar datos extra al response
        user = self.user

        data['tipo_usuario'] = self.user.tipo_usuario
        data['email'] = self.user.email
        data['username'] = self.user.username
        
        if user.tipo_usuario == 'ATLETA':
            try:
                atleta = user.atleta.get()  # relacionado con related_name='atleta'
                deporte_rel = AtletaDeporte.objects.get(atleta=atleta)
                data['deporte'] = deporte_rel.deporte.nombre
                data['nivel_habilidad'] = deporte_rel.nivel_habilidad
                data['deporte_id'] = deporte_rel.deporte.id
                data['id'] = atleta.id
            except Exception:
                data['deporte'] = None
                data['nivel_habilidad'] = None

        elif user.tipo_usuario == 'CLUB':
            try:
                admin_club = user.club.get()  # user.club por el related_name='club'
                club = admin_club.club
                data['deporte'] = club.deporte.nombre
                data['deporte_id'] = club.deporte.id
            except Exception:
                data['deporte'] = None
                data['deporte_id'] = None
        return data 
