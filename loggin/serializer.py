
# usuarios/serializers.p
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from atletas.models import AtletaDeporte
from clubes.models import Club  # Asegúrate de importar el modelo Club si es necesario  
from rest_framework import serializers
from django.contrib.auth import authenticate
from usuarios.models import Usuario


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    tipo_usuario = serializers.CharField(write_only=True)
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        tipo_usuario_enviado = attrs.pop('tipo_usuario', None)

        if username:
            username = username.upper()

        # Buscar usuario manualmente
        try:
            user_obj = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError({"detail": "Usuario no encontrado."})

        # Validar contraseña
        if not user_obj.check_password(password):
            raise serializers.ValidationError({"detail": "Contraseña incorrecta."})

        # Validar tipo de usuario
        if tipo_usuario_enviado.upper() != user_obj.tipo_usuario:
            raise serializers.ValidationError({"detail": "Tipo de usuario no coincide con el registrado."})

        # Autenticar formalmente (para que JWT valide el token)
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise serializers.ValidationError({"detail": "No se pudo autenticar el usuario."})

        self.user = user  # Necesario para que `super().validate()` funcione bien
        data = super().validate({'username': username, 'password': password})
        
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